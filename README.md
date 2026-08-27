# Sky Blog (Hexo + Sakura)

基于 [Hexo 8](https://hexo.io/) 与二次元风 [Sakura](https://github.com/honjun/hexo-theme-sakura) 主题的个人静态博客。

- 在线地址：https://zhixiaotx.github.io/skyblog/
- 源码分支：`main`（本仓库）
- 产物分支：`gh-pages`（构建出的静态文件）

> 本 README 是从零开始、把整套工程讲明白的"小白手册"。读完即可：
> 本地跑起来 → 写文章/换封面/换壁纸 → 推 GitHub → 一键部署到
> **GitHub Pages / Cloudflare Pages / Vercel / Netlify** 任一平台。

---

## 目录

1. [技术栈与特性](#1-技术栈与特性)
2. [仓库分支与部署总览](#2-仓库分支与部署总览)
3. [快速开始（30 秒跑起来）](#3-快速开始30-秒跑起来)
4. [目录结构详解（每个文件/夹的作用）](#4-目录结构详解每个文件夹的作用)
5. [写新文章](#5-写新文章)
6. [文章封面图（photos）设置](#6-文章封面图photos设置)
7. [壁纸（首页背景图）设置](#7-壁纸首页背景图设置)
8. [菜单 / 头像 / 音乐 / 社交配置](#8-菜单--头像--音乐--社交配置)
    - [8.5 背景音乐详细设置（换歌单/本地音乐/疑难）](#85-背景音乐详细设置换歌单--本地音乐--疑难解答)
9. [标签 / 分类页空白修复](#9-标签--分类页空白修复)
10. [移动端适配](#10-移动端适配)
11. [相对路径与子目录部署](#11-相对路径与子目录部署)
12. [部署指南](#12-部署指南)
    - [A. GitHub Pages（推荐：先推 `gh-pages` 再部署）](#a-github-pages推荐先推-gh-pages-再部署)
    - [B. Cloudflare Pages](#b-cloudflare-pages)
    - [C. Vercel](#c-vercel)
    - [D. Netlify](#d-netlify)
13. [GitHub Actions 自动化 CI](#13-github-actions-自动化-ci)
14. [常见问题与排错](#14-常见问题与排错)
15. [命令速查（CMD/PowerShell/Git Bash 都可）](#15-命令速查cmdpowershellgit-bash-都可)
16. [避坑清单（必读）](#16-避坑清单必读)

---

## 1. 技术栈与特性

| 模块 | 选型 | 说明 |
| --- | --- | --- |
| 框架 | Hexo 8 (`hexo@8.1.2`) | Node.js 静态博客 |
| 主题 | Sakura（已二次定制） | 二次元风格、动漫背景、APlayer 内嵌 |
| 部署 | GitHub Pages（`gh-pages` 分支） | 也兼容 Cloudflare/Vercel/Netlify |
| 文章渲染 | `hexo-renderer-marked` + `hexo-renderer-ejs/pug/stylus` | |
| 标签/分类 | `hexo-generator-tag` / `hexo-generator-category` | |
| 搜索 | `hexo-generator-search` + Insight 搜索 | |
| RSS | `hexo-generator-feed` → `atom.xml` | |
| 部署插件 | `hexo-deployer-git`（**本仓库禁用，见 §16**） | 仅作依赖保留 |
| 音乐 | 自定义 APlayer（`api.i-meto.com` + 网易云飙升榜） | 坏链自动切下一首 |
| 评论 | 暂未启用（Valine / Waline 留口） | |

---

## 2. 仓库分支与部署总览

```
┌────────────────────────────────────────────────────────┐
│ main（源码，Push 后 GitHub 看到的是这个分支）           │
│ ├─ _config.yml        站点主配置                        │
│ ├─ _config.sakura.yml Sakura 主题覆盖                   │
│ ├─ source/            文章/页面/图片源文件               │
│ ├─ themes/sakura/     主题（含已定制的 layout）          │
│ ├─ scaffolds/         文章/页面模板                     │
│ └─ package.json       依赖                              │
└────────────────────────────────────────────────────────┘
                          ↓  npx hexo g
┌────────────────────────────────────────────────────────┐
│ public/（构建产物，**不要**手动改）                     │
└────────────────────────────────────────────────────────┘
                          ↓  拷贝到独立部署仓
┌────────────────────────────────────────────────────────┐
│ gh-pages（产物，GitHub Pages 真正对外服务的分支）       │
└────────────────────────────────────────────────────────┘
                          ↓  GitHub Pages 自动发布
                   https://zhixiaotx.github.io/skyblog/
```

**两个分支互不干扰**：源码改动推 `main`；产物改动推 `gh-pages`。

---

## 3. 快速开始（30 秒跑起来）

### 前置

- **Node.js 16+**（推荐 18 或 20，本机用 22）
- **Git**
- 一个代码编辑器（VS Code 即可）

### 步骤

```bash
# 1. 克隆
git clone https://github.com/zhixiaotx/skyblog.git
cd skyblog

# 2. 安装依赖（首次或 package.json 变后）
npm install

# 3. 本地预览
npx hexo server
# 浏览器打开 http://localhost:4000/skyblog/
```

> 看到博客首页即成功。停服务按 `Ctrl + C`。

---

## 4. 目录结构详解（每个文件/夹的作用）

```
hexo-blog/
├── _config.yml                # 【站点主配置】标题/URL/语言/部署
├── _config.sakura.yml         # 【Sakura 主题覆盖配置】
├── _config_cf.yml             # 【Cloudflare 部署覆盖】url/root 改为根路径（见 §12.B）
├── package.json               # 【依赖清单】npm install 装这里
├── readme.md                  # 【本文档】
├── .gitignore                 # Git 忽略规则（public/node_modules 不入版本）
├── docs/                      # 项目文档（不参与部署）
│   └── 404-custom-backup.html # 404 渐变版备份（线上 404 如需回退用它）
├── .github/                   # （可选）GitHub Actions CI
│   └── workflows/
│       └── deploy.yml         # 自动构建 + 推送 gh-pages
│
├── source/                    # ★ 所有内容的源头
│   ├── 404.html               #   404 页（渐变+樱花+按钮，自定义版）
│   ├── _posts/                #   文章（Markdown）
│   │   ├── hello-world.md
│   │   ├── GitHub从入门到精通.md
│   │   └── 关于-GitHub-的一些事情.md
│   ├── about/index.md         #   关于页（layout: about 不需要）
│   ├── tags/index.md          #   ★ 标签根页（必须有，否则 /tags/ 404）
│   ├── categories/index.md    #   ★ 分类根页（必须有，否则 /categories/ 404）
│   └── img/                   #   图片资源
│       ├── favicon.png        #     浏览器标签小图标
│       ├── wallpaper/         #     8 张首页背景壁纸
│       │   ├── anime-scene.webp
│       │   ├── china-city.webp
│       │   ├── night-clouds.webp
│       │   ├── city-night.webp
│       │   ├── beach-sailboat.webp
│       │   ├── country-cottage.webp
│       │   ├── hammock.webp
│       │   └── bookshelf.webp
│       └── cover/             #   文章封面图（自己放）
│
├── themes/
│   └── sakura/                # ★ 主题（已定制，不要再 git clone 替换）
│       ├── _config.yml        #   主题默认配置（**改这里影响所有人**）
│       ├── layout/            #   EJS 模板（决定页面长什么样）
│       │   ├── index.ejs      #     首页
│       │   ├── post.ejs       #     文章页
│       │   ├── page.ejs       #     普通页
│       │   ├── archive.ejs    #     归档
│       │   ├── tag.ejs        #     ★ 标签页（根/单标签都走这里）
│       │   ├── category.ejs   #     ★ 分类页（同上）
│       │   ├── links.ejs      #     友人帐
│       │   ├── bangumi.ejs    #     番组
│       │   ├── donate.ejs     #     赞赏
│       │   ├── layout.ejs     #     全局骨架
│       │   ├── _partial/      #     片段（头/脚/菜单/播放器/分享）
│       │   └── _widget/       #     文章卡片/列表项
│       └── source/            #   主题自带 CSS/JS/字体
│           ├── css/style.css  #     ★ 已定制：菜单单行/间距/代码块颜色
│           ├── js/
│           └── fonts/
│
├── scaffolds/                 # 文章/页面/草稿的模板
│   ├── post.md                #   `hexo new` 用的模板
│   ├── page.md                #   `hexo new page` 用的模板
│   └── draft.md               #   草稿
│
└── public/                    # 【构建产物】hexo g 生成；不要手改；不入版本
```

**关键约定**

- 改主题配置 → 优先改 `_config.sakura.yml`（覆盖默认），别动 `themes/sakura/_config.yml`
- 改主题模板/样式 → 可以直接改 `themes/sakura/layout/*`、`themes/sakura/source/css/*`（已定制）
- 改菜单/封面 → 改 front matter 或配置文件，不要动 Markdown 正文外的 HTML

---

## 5. 写新文章

### 5.1 创建文章

```bash
npx hexo new "我的第一篇博客"
# 实际生成：source/_posts/我的第一篇博客.md
```

文件立刻可编辑。Front-matter（`---` 之间的 YAML）会自动生成：

```markdown
---
title: 我的第一篇博客
date: 2026-08-27 18:00:00
tags:
  - 技术
categories:
  - 生活
---
```

### 5.2 Front-matter 字段说明

| 字段 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- |
| `title` | ✅ | 文章标题 | `title: GitHub从入门到精通` |
| `date` | ✅ | 发布时间 | `date: 2026-08-27 15:07:00` |
| `updated` | – | 更新时间 | `updated: 2026-08-28 10:00:00` |
| `tags` | – | 标签（数组） | `tags: [技术, github]` |
| `categories` | – | 分类（数组） | `categories: [技术]` |
| `photos` | – | **封面/缩略图**（数组，第一张为封面） | `photos: [/img/cover/xx.jpg]` |
| `description` | – | 文章摘要 | `description: 一句话简介` |
| `comments` | – | 是否启用评论 | `comments: true` |
| `mathjax` | – | 是否启用数学公式 | `mathjax: true` |
| `top` | – | 置顶（数字越大越靠前） | `top: 100` |

### 5.3 写完预览

```bash
npx hexo server
# 浏览器看 http://localhost:4000/skyblog/
```

写完满意后：

```bash
npx hexo clean && npx hexo generate     # 重新生成 public/
# 然后走 §12 的部署流程
```

### 5.4 写独立页面（如" /留言" /" /清单"）

```bash
npx hexo new page comment       # 生成 source/comment/index.md
# 编辑 front-matter 写 layout: comment 等，详见对应模板
```

### 5.5 完整文章模板（直接复制改）

```markdown
---
title: 文章标题                  # 必填
date: 2026-08-27 21:00:00      # 必填
updated: 2026-08-27 21:00:00
tags:
  - 技术                        # 可多个
  - Hexo
categories:
  - 技术                        # 建议 1 个
photos:
  - /img/cover/your-cover.jpg   # 封面图（可选，第一张作封面/缩略图）
description: 一句话摘要，显示在首页列表
mathjax: false                  # 需要公式时改 true
---

正文从这里开始，用 Markdown 写。

## 二级标题

- 列表项
- **加粗**、*斜体*、`行内代码`

### 代码块（自动高亮，无行号）

```js
console.log("你好");
```

![图片说明](/img/post/xxx.png)
```

**写完发布的标准流程**：

```bash
npx hexo server                 # 1. 本地预览 http://localhost:4000/skyblog/
npx hexo clean && npx hexo generate   # 2. 重新生成 public/
git add . && git commit -m "post: 标题" && git push origin main   # 3. 推源码
# 4. 若配了 GitHub Actions（§13）→ 自动发布；否则走 §A.2 独立目录法推 gh-pages
```

---

## 6. 文章封面图（photos）设置

Sakura 主题用 **`photos` 数组**的第一张作为文章封面和列表缩略图。
（不是 `cover` 字段。）

### 6.1 推荐：本地图片

1. 把图片放到 `source/img/cover/`（目录不存在就 `mkdir`）：
   ```
   source/img/cover/my-article-cover.jpg
   ```
2. 在 front-matter 引用：
   ```markdown
   ---
   title: 我的文章
   photos:
     - /img/cover/my-article-cover.jpg
   ---
   ```

> `/` 开头是 Hexo 约定的"资源根"，Hexo 会自动加 `_config.yml` 里的 `root`（这里是 `/skyblog/`），
> 最终访问 `https://.../skyblog/img/cover/my-article-cover.jpg`。

### 6.2 远程图片（不推荐，慢）

```markdown
photos:
  - https://example.com/some-image.jpg
```

### 6.3 多张图（首页轮播/相册效果）

```markdown
photos:
  - /img/cover/01.jpg
  - /img/cover/02.jpg
```

列表缩略图用第一张；文章页头图也用第一张。

### 6.4 不设置封面

不写 `photos` 字段即可。文章页会用纯文字头部，无封面图。

---

## 7. 壁纸（首页背景图）设置

**入口**：背景图数组在 `themes/sakura/_config.yml` 的 `bg:` 字段。

### 7.1 修改步骤

1. 把壁纸放到 `source/img/wallpaper/`（统一 `.webp` 节省体积）
2. 改 `themes/sakura/_config.yml`：
   ```yaml
   bg:
     - /img/wallpaper/anime-scene.webp
     - /img/wallpaper/china-city.webp
     - /img/wallpaper/night-clouds.webp
     # ...共 8 张
   bgclass: ""   # 空=原图, filter-dim=阴影, filter-grid=横条, filter-dot=点点
   ```
3. **不要**同时在 `_config.sakura.yml` 里写 `bg:`，否则 Hexo 会拼接数组（16 张，前 8 张 CDN 裂图）

### 7.2 为什么必须用本地路径

Sakura 主题默认把 `bg` 拼 CDN 前缀，导致子目录部署（`/skyblog/`）时
图片访问路径错。本仓库的 `themes/sakura/layout/_partial/head.ejs` 已修复，
自动为每张背景图加 `url_for()` 子目录前缀。

### 7.3 添加更多壁纸

只要往 `source/img/wallpaper/` 加文件，然后在 `themes/sakura/_config.yml`
的 `bg:` 数组里加一行即可。

---

## 8. 菜单 / 头像 / 音乐 / 社交配置

**推荐改 `_config.sakura.yml`**（覆盖主题默认），不要直接动 `themes/sakura/_config.yml`。

### 8.1 菜单

```yaml
menus:
  首页:   { path: /, fa: fa-home }
  归档:   { path: /archives/, fa: fa-archive }
  标签:   { path: /tags/, fa: fa-tags }
  分类:   { path: /categories/, fa: fa-folder-open }
  清单:   { path: javascript:;, fa: fa-list-ul }
  留言板: { path: /comment/, fa: fa-pencil-square-o }
  友人帐: { path: /links/, fa: fa-link }
  关于:   { path: /about/, fa: fa-heart }
```

### 8.2 头像 / favicon

```yaml
favicon: /img/favicon.png
avatar:   /img/favicon.png
```

把图片放到 `source/img/favicon.png` 即可。

### 8.3 背景音乐（APlayer）

```yaml
aplayer:
  id: 19723756          # 网易云歌单 ID（飙升榜）
  server: netease
  type: playlist
  fixed: true           # 固定左下角
  autoplay: false        # 不要自动播放（浏览器策略）
  loop: all
  order: random
  preload: auto
  volume: 0.7
```

播放器模板在 `themes/sakura/layout/_partial/aplayer.ejs`，已重写为
**自定义 APlayer**（去掉 MetingJS）—— 坏链自动切下一首。

### 8.4 社交链接

PC 端（左下角图标）：
```yaml
social:
  github: { url: https://github.com/zhixiaotx, img: /img/social/github.png }
  email:  { url: mailto:liuliu19901110@gmail.com, img: /img/social/email.svg }
```

移动端（汉堡菜单里的图标按钮）：
```yaml
msocial:
  github: { url: https://github.com/zhixiaotx, fa: fa-github, color: 333 }
  email:  { url: mailto:liuliu19901110@gmail.com, fa: fa-envelope, color: dd4b39 }
```

### 8.5 背景音乐详细设置（换歌单 / 本地音乐 / 疑难解答）

播放器组件：`themes/sakura/layout/_partial/aplayer.ejs`（已重写为自定义 APlayer，
**去掉 MetingJS**，坏链自动切下一首）。数据源在 `_config.sakura.yml` 的 `aplayer:` 段。

#### 8.5.1 换一个网易云歌单（最常见需求）

```bash
# 1. 浏览器打开网易云音乐网页版，找到想用的歌单
#    https://music.163.com/#/playlist?id=19723756
# 2. 复制地址里 `id=` 后面的数字（19723756 就是歌单 ID）
```

改 `_config.sakura.yml`：

```yaml
aplayer:
  id: 19723756        # ★ 改成你的歌单 ID
  server: netease     # 数据源：网易云
  type: playlist      # 类型：歌单（不是单曲/专辑）
  fixed: true         # 固定显示在左下角
  autoplay: false     # 不要自动播放（浏览器会拦截）
  loop: all
  order: random
  preload: auto
  volume: 0.7
```

重新生成部署（§12）即可生效。

> 想换"单曲"就把 `type` 改成 `song`、`id` 填歌曲 ID；
> 想换"专辑"把 `type` 改成 `album`。

#### 8.5.2 各歌单可播率实测（网易云外链限制）

| 歌单 | ID | 实测可播率（前 12 首） |
| --- | --- | --- |
| 飙升榜 | `19723756` | ~70%（本项目当前使用） |
| 热歌榜 | `3778678` | ~40% |
| 学习纯音乐 | `486899256` | ~83% |
| 学习白噪音 | `2451877636` | ~83% |
| 重度失眠 | `884528449` | ~83% |
| 治愈温柔纯音乐 | `784227484` | ~83% |

> 网易云对 VIP/版权歌曲的外链全部失效（返回 404 或 size=0），
> 所以任何歌单都有一定比例放不了。本项目播放器已做"坏链自动跳下一首"，
> 体验优于官方 MetingJS（它会卡死在出错曲目）。

#### 8.5.3 彻底稳定方案：本地音乐文件

把 mp3 放到 `source/music/`，改播放器为本地列表
（`themes/sakura/layout/_partial/aplayer.ejs` 里的 audio 数组）：

```yaml
# 例如：在 aplayer.ejs 里用本地文件
audio:
  - name: 歌名1
    artist: 歌手1
    url: /music/1.mp3
    cover: /img/wallpaper/anime-scene.webp
  - name: 歌名2
    artist: 歌手2
    url: /music/2.mp3
    cover: /img/wallpaper/city-night.webp
```

本地文件路径以 `/` 开头会自动加 `/skyblog/` 前缀（`url_for`），
100% 可播、无版权限制、加载快。

#### 8.5.4 常见问题

- **一首歌放不了卡住**：网络歌单 VIP 歌 → 换歌单或换本地音乐方案。
- **完全没有声音/播放器不出现**：检查 `_config.sakura.yml` 的 `aplayer:` 是否被误删；
  `api.i-meto.com` 偶发 Cloudflare 403，刷新重试。
- **想彻底关闭音乐**：把 `aplayer:` 整段注释掉即可。

---

## 9. 标签 / 分类页空白修复

**症状**：点击菜单"标签"/"分类"显示空白或 404。
**根因**：没有 `source/tags/index.md` 和 `source/categories/index.md`，
hexo-generator-tag 只生成单标签页（如 `/tags/github/`），
不生成根索引页（`/tags/`）。

**修复**：

1. `source/tags/index.md`：
   ```markdown
   ---
   title: 标签
   layout: tag            # 注意：单数 tag，不是 type: tags
   description: 按标签浏览所有文章
   ---
   ```

2. `source/categories/index.md`：
   ```markdown
   ---
   title: 分类
   layout: category       # 注意：单数 category
   description: 按分类浏览所有文章
   ---
   ```

3. `themes/sakura/layout/tag.ejs` 和 `category.ejs` 已改造：
   - **根索引**（无 `page.tag` / `page.category`）→ 渲染标签/分类列表 + 文章数
   - **单标签/单分类页** → 渲染文章列表（原行为）

**注意**：Sakura 只有 `tag.ejs`（单数），所以 front-matter 必须写 `layout: tag`，
不能用 `type: tags`（会找不到 `tags.ejs` 而回退到 `page.ejs`）。

---

## 10. 移动端适配

### 10.1 现状

- 主题自带 `@media` 响应式：手机访问会自动隐藏侧栏、压缩字体
- 菜单单行（已定制）：`themes/sakura/source/css/style.css`：
  ```css
  .site-top .lower nav.navbar ul { display:flex; flex-wrap:nowrap; white-space:nowrap }
  .site-top .lower nav.navbar ul li { float:none; flex-shrink:0; white-space:nowrap; margin:0 15px }
  ```
- 移动端汉堡菜单：自动启用

### 10.2 自适应优化建议

- 字体大小：编辑 `themes/sakura/source/css/style.css` 的 `@media (max-width: 768px)` 块
- 背景图：移动端建议压缩到 ≤ 200KB（用 `.webp`）
- 播放器：移动端会自动收起为底部条
- 触摸目标 ≥ 44×44 px（菜单间距已调到 15px 满足）

### 10.3 测试设备

```bash
# Chrome 开发者工具 → Toggle device toolbar (Ctrl+Shift+M)
# 测试宽度：375 (iPhone SE) / 768 (iPad) / 1280 (Desktop)
```

---

## 11. 相对路径与子目录部署

本博客部署在 `https://zhixiaotx.github.io/skyblog/`，**子目录 `/skyblog/`** 是 GitHub Pages
project site 的标志。

### 11.1 `_config.yml` 里的关键配置

```yaml
url: https://zhixiaotx.github.io/skyblog
root: /skyblog/                       # ★ 所有 url_for() 自动加此前缀
permalink: :year/:month/:day/:title/
pretty_urls:
  trailing_index: true               # /tags/ 等同于 /tags/index.html
```

### 11.2 主题里的坑

Sakura 主题的部分 `ejs` 直接拼路径，不加 `url_for()`，会导致子目录部署裂图。
**本仓库已修复的清单**：

| 文件 | 问题 | 修复 |
| --- | --- | --- |
| `themes/sakura/layout/_partial/head.ejs` | `var bg = theme.bg` 没加子目录前缀 | 用 `url_for(b)` 包裹 |
| `themes/sakura/layout/_partial/startdash.ejs` | START:DASH 图片拼 CDN | 以 `/` 开头则走 `url_for()` |
| `themes/sakura/layout/_partial/headertop.ejs` | 头像拼 CDN | 以 `/` 开头则走 `url_for()` |

**通用规则**：在主题里看到路径拼接（特别是 `theme.cdn + ...` 或 `theme.xxx + ...`），
要警惕子目录部署问题。优先用 `url_for()`。

---

## 12. 部署指南

### A. GitHub Pages（推荐：先推 `gh-pages` 再部署）

**当前生产方案**——手动构建 + 独立部署仓 + force push，避免 hexo-deployer-git
把源码误推到 gh-pages（详见 §16）。

#### A.1 一次性准备

仓库 Settings → Pages → Source 选 **`gh-pages`** 分支，根目录 `/`。

#### A.2 每次部署

```bash
cd hexo-blog
npx hexo clean && npx hexo generate

# 拷贝产物到独立部署目录
rm -rf D:\skyblog_fix_new\*              # 清空旧产物（保留 .git 和 .nojekyll）
cp -r public/* D:\skyblog_fix_new/
touch D:\skyblog_fix_new/.nojekyll       # 跳过 Jekyll 构建

cd D:\skyblog_fix_new
git add -A
git -c http.version=HTTP/1.1 commit -m "Site updated: $(date +'%Y-%m-%d %H:%M')"
git -c http.version=HTTP/1.1 push -f origin HEAD:gh-pages
```

> `http.version=HTTP/1.1` 是为了避开代理的 HTTP/2 + TLS 兼容问题。如果直连没问题，去掉即可。

#### A.3 用 `hexo d`？

**禁止**。详见 §16，会把源码 push 到 gh-pages。

#### A.4 自动模式：见 §13 GitHub Actions

---

### B. Cloudflare Pages

**优点**：全球 CDN、自动 HTTPS、支持自定义域名、免费。
**注意**：Cloudflare Pages 的 **Framework preset 没有 Hexo 选项**（这正常），选 `None` 后手动填即可。

#### B.0 前提：`_config_cf.yml`（解决样式丢失的关键）

仓库根目录已有 `_config_cf.yml`，它的作用是**覆盖 GitHub Pages 的子目录配置**：

```yaml
url: https://你的项目名.pages.dev   # 改成你的实际 pages.dev 域名
root: /                              # Cloudflare 部署在域名根，不是 /skyblog/ 子目录
```

> ⚠️ **为什么必须有它**：源码 `_config.yml` 的 `root: /skyblog/` 是给 GitHub Pages 子目录用的。
> 不覆盖就部署到 Cloudflare，HTML 里所有资源还是 `/skyblog/css/...` → 域名根下 404 →
> **页面变成裸 HTML（乱码/样式全丢）**。多 config 合并是官方支持的标准做法，
> 且不影响 GitHub Pages 的 main 分支配置。

#### B.1 步骤

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → Pages
2. **Connect to Git** → 选 GitHub → 选 `zhixiaotx/skyblog`
3. **Build settings**（Framework preset 选 **None**，手动填）：

   | 项 | 值 |
   | --- | --- |
   | Framework preset | **None**（Cloudflare 没有 Hexo 预设） |
   | Build command | `npx hexo generate --config _config.yml,_config_cf.yml` |
   | Build output directory | `public` |
   | Root directory | `hexo-blog`（如果 monorepo；纯仓库留空） |
   | Node version | `20`（环境变量 `NODE_VERSION=20`） |

4. **Environment variables**（Production）：

   | 变量 | 值 |
   | --- | --- |
   | `NODE_VERSION` | `20` |
   | `PUBLIC_URL` | `https://your-project.pages.dev` |

5. **Save and Deploy**。等 1-2 分钟，构建完即可访问。

> 构建命令里的 `--config _config.yml,_config_cf.yml` 是 Hexo 的**多配置合并**语法：
> 主配置 + CF 覆盖，后者优先级更高。改 `_config_cf.yml` 后 push 到 GitHub，
> Cloudflare 会自动重新构建。

#### B.2 自定义域名

Pages 项目 → Custom domains → `blog.yourname.com`
→ Cloudflare 自动加 CNAME 和 HTTPS。

#### B.3 备选：部署 `gh-pages` 分支（更简单）

如果不想要构建过程，Cloudflare 也可以**直接部署现成的 `gh-pages` 分支**：

| Build settings | 值 |
| --- | --- |
| Framework preset | None |
| Build command | （留空） |
| Build output directory | `/` |
| 分支 | `gh-pages`（Connect to Git 时选） |

零配置、不用管 `_config_cf.yml`，跟着 GitHub Pages 的工作流走即可。

#### B.4 构建失败排查

**症状**：日志出现 `Installing project dependencies: yarn` 然后
`YN0028: The lockfile would have been modified by this install`，exit 1。

**原因**：仓库里同时存在 `package-lock.json`（npm）和 `yarn.lock`（yarn）。
Cloudflare 检测到 `yarn.lock` 就强制用 **Yarn 4** 装依赖，而 Yarn 4 的
"不可变安装"发现 lockfile 需要更新就直接报错。

**解决**：只保留一种包管理器的锁文件。本仓库用 npm：

```bash
git rm yarn.lock          # 删除 yarn.lock（保留 package-lock.json）
git commit -m "fix: 删除 yarn.lock"
git push origin main
```

重新 Save and Deploy，日志应变为 `Installing project dependencies: npm`。

> 判断依据：Cloudflare 按"有 `yarn.lock` 用 yarn，否则有 `package-lock.json` 用 npm"选择
> 包管理器。所以**别让两种锁文件同时存在**。

---

### C. Vercel

**优点**：零配置、自动预览（PR）、全球 CDN。

#### C.1 步骤

1. 登录 [Vercel](https://vercel.com/) → New Project
2. **Import Git Repository** → 选 `zhixiaotx/skyblog`
3. **Configure Project**：

   | 项 | 值 |
   | --- | --- |
   | Framework Preset | Other |
   | Build Command | `npm run build` |
   | Output Directory | `public` |
   | Install Command | `npm install` |

4. **Deploy**。30 秒后拿到 `xxx.vercel.app` URL。

#### C.2 环境变量

Project Settings → Environment Variables：

| Key | Value |
| --- | --- |
| `PUBLIC_URL` | `https://xxx.vercel.app` |

---

### D. Netlify

**优点**：表单/函数/CDN 一体、Git LFS 支持好。

#### D.1 步骤

1. 登录 [Netlify](https://app.netlify.com/) → Add new site → Import existing project
2. 选 GitHub → 选 `zhixiaotx/skyblog`
3. **Build settings**：

   | 项 | 值 |
   | --- | --- |
   | Base directory | `hexo-blog`（monorepo 时） |
   | Build command | `npm run build` |
   | Publish directory | `hexo-blog/public` |
   | Functions directory | （留空） |

4. **Deploy site**。

#### D.2 自定义域名

Site settings → Domain management → Add custom domain。

---

## 13. GitHub Actions 自动化 CI

让 push `main` 后**自动**构建并推 `gh-pages`。

### 13.1 创建工作流文件

`.github/workflows/deploy.yml`：

```yaml
name: Deploy Hexo to gh-pages

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install
        run: npm ci

      - name: Build
        run: npx hexo generate

      - name: Deploy to gh-pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          publish_branch: gh-pages
          force_orphan: true
          user_name: 'github-actions[bot]'
          user_email: 'github-actions[bot]@users.noreply.github.com'
```

### 13.2 启用

`git add .github/workflows/deploy.yml && git commit && git push origin main`
→ Settings → Actions → 启用 workflow → 每次推 main 都会自动部署到 gh-pages。

### 13.3 优缺点

| 优点 | 缺点 |
| --- | --- |
| 一键 push 即部署 | 首次配 SSH/Token |
| 构建在云端，本地无需 Node | 调试要等 CI 完成 |
| PR 可预览 | Actions 有时长限制 |

---

## 14. 常见问题与排错

### Q1. 标签/分类页空白 / 404

**原因**：缺 `source/tags/index.md` 或 `source/categories/index.md`。
**解决**：见 §9。

### Q2. 壁纸不显示 / 显示 CDN 默认图

**原因 A**：`themes/sakura/_config.yml` 和 `_config.sakura.yml` 同时写了 `bg:`
→ 数组拼接成 16 张，前 8 张是 CDN（404）。
**解决**：**只在 `themes/sakura/_config.yml` 写本地壁纸**，从 `_config.sakura.yml` 删除 `bg:`。

**原因 B**：`var bg` 渲染的路径缺 `/skyblog/` 子目录前缀。
**解决**：见 §11.2，head.ejs 已修。

### Q3. 文章封面图不显示

**原因**：用了 `cover:` 字段。Sakura 用的是 **`photos:`** 数组。
**解决**：见 §6。若路径以 `/` 开头但还裂图，通常是**缺 `/skyblog/` 子目录前缀**——
本项目已在 `common-article.ejs`、`category-items.ejs`、`index-items.ejs` 全部用
`url_for()` 包裹，`photos: [/img/cover/xxx.jpg]` 会自动加前缀。

### Q4. 网易云音乐播放不了

**原因**：网易云外链 80% 都失效（VIP/版权）。
**解决**：换歌单 ID（已用飙升榜 `19723756`）+ 坏链自动跳下一首（自定义 APlayer）。彻底稳
定方案：把 mp3 放到 `source/music/`，改 APlayer 用本地列表。

### Q5. `git push` 失败 SSL 握手 / Connection reset

**原因**：本机代理与 GitHub 的 HTTP/2 + TLS 不兼容，或代理挂了。
**解决（按顺序试）**：

```bash
# 方案 1：用 HTTP/1.1
git -c http.version=HTTP/1.1 push origin main

# 方案 2：绕过代理直连（Git Bash）
env -u HTTP_PROXY -u HTTPS_PROXY git -c http.proxy= -c https.proxy= \
  -c http.version=HTTP/1.1 push origin main
```

### Q6. `hexo d` 后 GitHub Pages 挂了（404 / 显示源码）

**原因**：`hexo-deployer-git` 在站点根目录本身是 git 仓库时，会把**整个源码**
推送到 gh-pages。
**解决**：**禁用 hexo d**，改用 §A.2 的"独立目录 cp + force push"流程。
详见 §16。

### Q7. 启动 `hexo s` 报文件锁 / 端口占用

```bash
# 杀进程
npx hexo s --debug 2>&1 | grep -i lock
# Windows:
Get-Process node | Stop-Process -Force    # PowerShell
# 或
taskkill /F /IM node.exe                  # CMD
```

### Q8. 代码块每行前面有数字（行号）想去掉

**原因**：`_config.yml` 的 `highlight.line_number: true`。
**解决**：改成 `line_number: false`（本仓库已改），重新生成即只剩代码。

### Q9. 首页文章缩略图显示"猫图"

**原因**：封面路径缺 `/skyblog/` 前缀 → 加载失败 → `onerror` 兜底到 CDN 的
`image-404.png`（猫图）。本项目已在 `index-items.ejs` 修复，
只要文章 `photos:` 写对（见 §6）就显示封面。

### Q10. Cloudflare Pages 构建失败：`YN0028` / `yarn.lock`

**原因**：仓库同时存在 `package-lock.json` 和 `yarn.lock`，Cloudflare 选了
Yarn 4 并因 lockfile 不一致报错。
**解决**：`git rm yarn.lock` 删掉只留 npm 的锁文件（见 §12.B.4），重新部署。

---

## 15. 命令速查（CMD/PowerShell/Git Bash 都可）

> 本机推荐用 **Git Bash**（Windows 已自带）。

| 用途 | 命令 |
| --- | --- |
| 装依赖 | `npm install` |
| 本地预览 | `npx hexo server` |
| 创建文章 | `npx hexo new "标题"` |
| 创建独立页 | `npx hexo new page 路径` |
| 生成静态文件 | `npx hexo generate` |
| 清缓存 | `npx hexo clean` |
| 一键生成+部署（**禁用**） | ~~`npx hexo deploy -g`~~ |
| 推源码 | `git push origin main` |
| 推产物（force） | `git -c http.version=HTTP/1.1 push -f origin HEAD:gh-pages` |
| 看 git 状态 | `git status` |
| 看提交历史 | `git log --oneline -20` |
| 临时 HTTP 服务器（调试） | `npx http-server public -p 8080` |

### 常用 Git Bash 命令

```bash
# 列文件
ls -la
# 看大小
du -sh 文件名
# 搜索内容
grep -rn "关键词" 路径/
# 移动
mv src dst
# 复制（递归）
cp -r src dst
```

### 常用 PowerShell 命令（Windows 管理员）

```powershell
Get-Process node                    # 看 node 进程
Stop-Process -Name node -Force      # 杀 node
Get-ChildItem                       # 列文件（= ls）
Remove-Item xxx -Recurse -Force     # 删（小心！）
```

---

## 16. 避坑清单（必读）

### 🚨 1. 禁用 `hexo d`

`hexo deploy` 配合 `hexo-deployer-git` 在"站点根目录本身是 git 仓库"时，
`.deploy_git` 共享根 `.git` → `git add -A` 作用于整个工作区 → **把源码推到 gh-pages**，
GitHub Pages 看到 404（没有根 `index.html`）。

**强制规范**：本仓库**只用独立目录法**部署（§A.2）。

### 🚨 2. Hexo 主题配置数组是 concat 不是 replace

`_config.{theme}.yml` 和 `themes/{theme}/_config.yml` 同名数组字段是**拼接**
不是覆盖。`bg`、`startdash`、`menus.submenus` 都会拼。

**原则**：同名数组**只在一边配置**，另一边彻底删。

### 🚨 3. 子目录部署必须用 `url_for()`

所有"拼字符串拼出路径"的位置，**优先用 `url_for()`**，
否则 `/skyblog/` 子目录会 404。

### 🚨 4. 改主题前先备份

`themes/sakura/` 是 git 子目录。改之前 `git status` 看一眼，
改完 `git diff` 检查。

### 🚨 5. Sakura 的 `tag.ejs` 是单数

front-matter 写 `layout: tag` 和 `layout: category`，**不要**写
`type: tags`/`type: categories`（找不到 `tags.ejs`，回退 `page.ejs`）。

### 🚨 6. GitHub Pages 必须 `.nojekyll`

不加的话 Jekyll 静默失败时，会沿用旧构建、表现为"提交已上但线上不变"。
**务必** `touch .nojekyll`。

### 🚨 7. 代理推送三板斧

```bash
# ① 默认代理
git push origin main

# ② HTTP/1.1（解决 HTTP/2 + 代理 TLS 不兼容）
git -c http.version=HTTP/1.1 push origin main

# ③ 直连（绕过代理）
env -u HTTP_PROXY -u HTTPS_PROXY git -c http.proxy= -c https.proxy= \
  -c http.version=HTTP/1.1 push origin main
```

### 🚨 8. `url_for()` 要覆盖"所有"文章列表模板

Sakura 的文章卡片有 **3 套**：首页 `_widget/index-items.ejs`、
分类/标签页 `_widget/category-items.ejs`、文章页 `_widget/common-article.ejs`。
凡用到 `post.photos[0]` 的地方都必须 `url_for()` 包裹，漏一套就会在该处裂图
（首页裂图会 `onerror` 兜底成 CDN 猫图 `image-404.png`）。

### 🚨 9. 代码块行号开关在 `_config.yml`

```yaml
highlight:
  line_number: false   # true = 每行前有数字；false = 只要代码
```

改了要 `hexo clean && hexo generate` 才生效。

### 🚨 10. 别让 npm 和 yarn 的锁文件同时存在

`package-lock.json` 和 `yarn.lock` 同时在仓库里，Cloudflare/CI 会优先用
`yarn.lock` → Yarn 4 → `YN0028` 报错。**只用一种包管理器**，本项目用 npm
（见 §12.B.4）。

---

## 许可证

本项目代码 MIT 协议。Sakura 主题遵循其原作者协议。
文章内容版权归原作者所有（转载文章已注明来源）。

本仓库源码 MIT。Sakura 主题遵循其原作者协议。
文章内容版权归原作者所有（转载文章已注明来源）。

## 致谢

- [Hexo](https://hexo.io/)
- [Sakura](https://github.com/honjun/hexo-theme-sakura)
- [APlayer](https://github.com/DIYgod/APlayer)