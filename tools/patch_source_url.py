#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给已抓取的 84 篇文章 front-matter 补 source_url 字段（幂等，重复运行不叠加）"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "source", "_posts")

patched = 0
skipped = 0

for path in glob.glob(os.path.join(POSTS, "*.md")):
    name = os.path.basename(path)
    if not re.match(r"^\d+-", name):  # 只处理抓取的文章（id- 前缀）
        continue

    with open(path, encoding="utf-8") as f:
        text = f.read()

    if "source_url:" in text:
        skipped += 1
        continue

    # 从文末署名行提取原文链接
    m = re.search(r"\[Ai星码博客\]\((https://aixmb\.com/\d+\.html)\)", text)
    if not m:
        print(f"WARN 未找到原文链接: {name}")
        continue
    source_url = m.group(1)

    # 在 front-matter 结束符之前插入
    # 注意：必须从第 1 行往后找「第 2 个 ---」（front-matter 结束符），
    # 不能从后往前找 —— 文末署名前也有一个 ---，会插错位置。
    lines = text.split("\n")
    insert_at = None
    for i in range(1, min(len(lines), 30)):
        if lines[i].strip() == "---":
            insert_at = i
            break
    if insert_at is None:
        print(f"WARN 无 front-matter 结束符: {name}")
        continue

    lines.insert(insert_at, f"source_url: {source_url}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    patched += 1

print(f"已补 source_url: {patched} 篇，跳过(已有): {skipped} 篇")
