#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 aixmb.com (WordPress) 抓取文章，转换为 Hexo Sakura 主题可用的 Markdown。

规则：
- 保留原作者署名 + 原文链接（source_url / 文末 attribution）
- 移除「视频讲解：/ YouTube：/ 哔哩哔哩：」块
- 封面走 photos: 数组（Sakura 主题机制），图片本地化到 source/img/aixmb/
- 正文图片 data-src 是真实地址，src 是占位图 -> 下载真实图并改写路径
"""

import os
import re
import json
import time
import hashlib
from urllib.parse import urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE = "https://aixmb.com"
API = BASE + "/wp-json/wp/v2"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(ROOT, "source", "_posts")
IMG_DIR = os.path.join(ROOT, "source", "img", "aixmb")
STATE_FILE = os.path.join(ROOT, "tools", ".aixmb_state.json")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
SESSION = requests.Session()
SESSION.headers.update(HEADERS)

ATTRIBUTION = "\n\n---\n\n> 本文转载自 [AI星码](https://aixmb.com/)，原文链接：[%s](%s)\n"


# ---------- 工具函数 ----------

def fetch_json(url, retries=3):
    for i in range(retries):
        try:
            r = SESSION.get(url, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(1.5 * (i + 1))


def clean_text(html):
    """HTML -> 纯文本（去标签、解实体）"""
    return BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)


def yaml_quote(s):
    """YAML 双引号转义"""
    s = str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return '"' + s + '"'


def safe_filename(title, pid):
    """生成安全文件名：清理 Windows 非法字符，截断，附加 id 防重"""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", title).strip()
    name = re.sub(r"\s+", "-", name)
    name = name[:60] or "post"
    return f"aixmb-{pid}-{name}.md"


def is_video_block(text):
    """识别「视频讲解 / YouTube / 哔哩哔哩」标题块"""
    t = text.strip().rstrip("：:")
    return t in ("视频讲解", "YouTube", "哔哩哔哩", "视频讲解 ", "YouTube ", "哔哩哔哩 ") or \
        t.startswith("视频讲解") or t.startswith("YouTube") or t.startswith("哔哩哔哩")


def download_image(url, cache):
    """下载图片到本地，返回 Hexo 路径 /img/aixmb/xxx.ext；失败返回 None"""
    if not url or not url.startswith("http"):
        return None
    url = url.replace("&amp;", "&")
    key = hashlib.md5(url.encode("utf-8")).hexdigest()
    if key in cache:
        return cache[key]

    ext = os.path.splitext(urlparse(url).path)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"):
        ext = ".png"
    filename = key[:16] + ext
    local_path = os.path.join(IMG_DIR, filename)
    rel_path = "/img/aixmb/" + filename

    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        cache[key] = rel_path
        return rel_path

    try:
        r = SESSION.get(url, timeout=30)
        r.raise_for_status()
        if len(r.content) < 100:
            return None
        with open(local_path, "wb") as f:
            f.write(r.content)
        cache[key] = rel_path
        return rel_path
    except Exception:
        return None


def convert_content(html, img_cache, stats):
    """正文 HTML -> Markdown，同时移除视频块、本地化图片"""
    soup = BeautifulSoup(html or "", "html.parser")

    # 1) 移除「视频讲解 / YouTube / 哔哩哔哩」块（可能是 h2/p/div）
    removed = 0
    for el in list(soup.find_all(["h1", "h2", "h3", "h4", "h5", "p", "div", "span"])):
        if is_video_block(el.get_text(" ", strip=True)):
            # 只移除自身，不动子元素；decompose 会连带子标签
            el.decompose()
            removed += 1
    stats["video_blocks_removed"] += removed

    # 2) 图片本地化：data-src 才是真实地址，src 是占位图
    for img in soup.find_all("img"):
        real = img.get("data-src") or img.get("data-original") or img.get("src")
        if real and "thumbnail-lg.svg" in real:
            # 占位图：尝试 data-src
            real = img.get("data-src") or img.get("data-original")
        if not real:
            img.decompose()
            continue
        local = download_image(real, img_cache)
        if local:
            img["src"] = local
            stats["images_localized"] += 1
        else:
            stats["images_failed"] += 1
            img["src"] = real
        # 清理懒加载属性，避免 markdownify 带出奇怪内容
        for attr in ("data-src", "data-original", "srcset", "class", "loading", "decoding", "width", "height"):
            if attr in img.attrs:
                del img[attr]

    # 3) 移除 onclick / 脚本残留
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.startswith("on") or attr in ("mce-contenteditable",):
                del tag.attrs[attr]

    # 4) HTML -> Markdown
    text = md(
        str(soup),
        heading_style="ATX",
        bullets="-",
        code_language="",
    )
    # markdownify 有时会给代码块加多余语言标记，清理空语言行
    text = re.sub(r"```\s*\n", "```\n", text)
    # 压缩 3+ 空行为 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_frontmatter(post, cats_map, tags_map, cover_path, stats):
    title = clean_text(post["title"]["rendered"])
    date = post["date"].replace("T", " ")
    modified = post["modified"].replace("T", " ")
    link = post["link"]

    categories = [cats_map.get(cid, "未分类") for cid in post.get("categories", [])]
    tags = [tags_map.get(tid) for tid in post.get("tags", [])]
    tags = [t for t in tags if t and t != "关于本站"]  # "关于本站"无意义，剔除

    desc = clean_text(post.get("excerpt", {}).get("rendered", ""))
    if len(desc) > 160:
        desc = desc[:160] + "..."

    lines = ["---", f"title: {yaml_quote(title)}", f"date: {yaml_quote(date)}", f"updated: {yaml_quote(modified)}"]

    if tags:
        lines.append("tags:")
        for t in tags:
            lines.append(f"  - {yaml_quote(t)}")
    if categories:
        lines.append("categories:")
        for c in categories:
            lines.append(f"  - {yaml_quote(c)}")
    if cover_path:
        lines.append("photos:")
        lines.append(f"  - {yaml_quote(cover_path)}")
        stats["with_cover"] += 1

    lines += [
        f"description: {yaml_quote(desc)}",
        f"source_url: {yaml_quote(link)}",
        "author: " + yaml_quote("AI星码"),
        "---",
        "",
    ]
    return "\n".join(lines)


def process_post(post, cats_map, tags_map, img_cache, stats, overwrite=False):
    title = clean_text(post["title"]["rendered"])
    filename = safe_filename(title, post["id"])
    out_path = os.path.join(POSTS_DIR, filename)

    if os.path.exists(out_path) and not overwrite:
        stats["skipped"] += 1
        return ("skip", filename)

    # 封面
    cover_path = None
    mid = post.get("featured_media", 0)
    if mid:
        try:
            media = fetch_json(f"{API}/media/{mid}")
            cover_url = media.get("source_url")
            cover_path = download_image(cover_url, img_cache)
        except Exception:
            pass

    fm = build_frontmatter(post, cats_map, tags_map, cover_path, stats)
    body = convert_content(post["content"]["rendered"], img_cache, stats)
    attribution = ATTRIBUTION % (title, post["link"])
    content = fm + body + attribution + "\n"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    stats["written"] += 1
    return ("ok", filename)


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMG_DIR, exist_ok=True)

    # 断点状态（图片缓存）
    img_cache = {}
    if os.path.exists(STATE_FILE):
        try:
            img_cache = json.load(open(STATE_FILE, encoding="utf-8"))
        except Exception:
            pass

    print(">>> 拉取分类/标签...")
    cats = {c["id"]: c["name"] for c in fetch_json(f"{API}/categories?per_page=100")}
    tags = {t["id"]: t["name"] for t in fetch_json(f"{API}/tags?per_page=100")}
    print(f"    分类 {len(cats)} 个，标签 {len(tags)} 个")

    print(">>> 拉取全部文章...")
    posts = []
    page = 1
    while True:
        batch = fetch_json(f"{API}/posts?per_page=50&page={page}")
        if not batch:
            break
        posts.extend(batch)
        print(f"    第 {page} 页: {len(batch)} 篇 (累计 {len(posts)})")
        page += 1
        if len(batch) < 50:
            break
    print(f"    共 {len(posts)} 篇")

    stats = {
        "written": 0, "skipped": 0, "with_cover": 0,
        "images_localized": 0, "images_failed": 0,
        "video_blocks_removed": 0,
    }

    # 串行处理（API 有速率限制，图片下载在单篇内同步，但可以并发文章）
    for i, post in enumerate(posts, 1):
        try:
            status, name = process_post(post, cats, tags, img_cache, stats)
            if status == "ok":
                print(f"[{i:3d}/{len(posts)}] OK   {name}")
            else:
                print(f"[{i:3d}/{len(posts)}] SKIP {name}")
        except Exception as e:
            print(f"[{i:3d}/{len(posts)}] FAIL id={post['id']}: {e}")
        if i % 20 == 0:
            json.dump(img_cache, open(STATE_FILE, "w", encoding="utf-8"), ensure_ascii=False)

    json.dump(img_cache, open(STATE_FILE, "w", encoding="utf-8"), ensure_ascii=False)

    print("\n========== 统计 ==========")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print(f"生成目录: {POSTS_DIR}")
    print(f"图片目录: {IMG_DIR}")


if __name__ == "__main__":
    main()
