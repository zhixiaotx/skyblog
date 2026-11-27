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
17. [赞赏（"赏"）二维码：换成自己的收款码](#17-赞赏赏二维码换成自己的收款码)
18. [批量导入外部博客文章（84 篇实战）](#18-批量导入外部博客文章84-篇实战)
19. [页脚署名 / 版权文字怎么改](#19-页脚署名--版权文字怎么改)
20. [音乐播放器（myhkw 免插件版）](#20-音乐播放器myhkw-免插件版)
21. [首页头像与头像下方的社交链接](#21-首页头像与头像下方的社交链接)
22. [导航栏站名左边加头像](#22-导航栏站名左边加头像)
23. [去掉标题后面的 ¶ 符号](#23-去掉标题后面的--符号)
24. [关掉头部背景视频（不自动播放）](#24-关掉头部背景视频不自动播放)
25. [看板娘挪到左侧 + 社交图标改回品牌色](#31-看板娘挪到左侧--社交图标改回品牌色)（正文编号 §31）
26. [移动端页脚与电脑端署名统一](#32-移动端页脚与电脑端署名统一)（正文编号 §32）

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

## 17. 赞赏（"赏"）二维码：换成自己的收款码

文章页/独立页底部那个红色 **赏** 按钮，点开弹出的两张图（支付宝、微信）就是赞赏码。
它**不是**文章内容，而是主题模板 + 主题配置渲染出来的。

### 17.1 相关位置一览

| 环节 | 文件 | 说明 |
| --- | --- | --- |
| 图片文件 | `source/img/custom/donate/AliPayQR.jpg`、`WeChanQR.jpg`、`WeChanSQ.jpg` | 目录不存在就自己建；文件名可改，但要和配置一致 |
| 路径配置（主题默认） | `themes/sakura/_config.yml` → `donate:` | 见 17.2 |
| 路径配置（站点覆盖，推荐改这里） | `_config.sakura.yml` | 同名字段优先级更高 |
| 渲染模板 | `themes/sakura/layout/_widget/common-article.ejs`（文章页）第 47-56 行、`common-page.ejs`（独立页）第 18-26 行 | 真正拼出 `<img src>` 的地方 |
| 打赏独立页 | `themes/sakura/layout/donate.ejs` 第 63-65 行 | 同一套 QR 变量 |

主题默认值：

```yaml
donate:
  paypal: https://www.paypal.me/hojuncn
  alipay: /img/custom/donate/AliPayQR.jpg   # 支付宝
  wechat: /img/custom/donate/WeChanQR.jpg   # 微信（文章页弹窗用这张）
  wechatSQ: /img/custom/donate/WeChanSQ.jpg # 微信（打赏页用这张）
```

### 17.2 关键坑：CDN 前缀会盖掉本地图（本项目已修复）

模板里写的是：

```ejs
<img src="<%- (theme.cdn || '') + theme.donate.alipay %>">
```

而 `_config.sakura.yml` 里有 `cdn: https://cdn.jsdelivr.net/gh/honjun/cdn@1.6`，
于是线上实际加载的是：

```
https://cdn.jsdelivr.net/gh/honjun/cdn@1.6/img/custom/donate/AliPayQR.jpg
```

——**这是 Sakura 原作者 honjun 的收款码**，你往 `source/img/custom/donate/` 放新图也不会被用到。

> 2026-11-26 本项目已修复：三处模板改成 `url_for()`，并把收款码换成自己的（见 17.5）。

### 17.3 换成自己收款码（推荐做法）

1. 准备两张正方形收款码，放进 `hexo-blog/source/img/custom/donate/`：
   ```
   source/img/custom/donate/AliPayQR.jpg     # 支付宝
   source/img/custom/donate/WeChanQR.jpg     # 微信
   source/img/custom/donate/WeChanSQ.jpg     # 微信（打赏页，可选）
   ```
2. 把模板里的 CDN 拼接改成 `url_for()`（`common-article.ejs`、`common-page.ejs`、`donate.ejs` 三处一起改）：

   ```ejs
   <!-- 改前 -->
   <li class="alipay-code"><img src="<%- (theme.cdn || '') + theme.donate.alipay%>"></li>
   <li class="wechat-code"><img src="<%- (theme.cdn || '') + theme.donate.wechat%>"></li>

   <!-- 改后：http(s):// 完整外链直接用，/img/... 本地路径自动加 /skyblog/ 前缀 -->
   <li class="alipay-code"><img src="<%- /^https?:\/\//.test(theme.donate.alipay) ? theme.donate.alipay : url_for(theme.donate.alipay) %>"></li>
   <li class="wechat-code"><img src="<%- /^https?:\/\//.test(theme.donate.wechat) ? theme.donate.wechat : url_for(theme.donate.wechat) %>"></li>
   ```

3. 在 `_config.sakura.yml` 里显式声明（方便以后换图，不用动主题）：

   ```yaml
   donate:
     alipay: /img/custom/donate/AliPayQR.jpg
     wechat: /img/custom/donate/WeChanQR.jpg
     wechatSQ: /img/custom/donate/WeChanSQ.jpg
   ```

4. 重新生成并预览：

   ```bash
   npx hexo clean && npx hexo generate
   npx hexo server        # 打开任意文章，点"赏"看弹窗图片是否换成自己的
   ```

### 17.4 想彻底不显示"赏"

把 `themes/sakura/layout/_widget/common-article.ejs` 第 47-56 行整块
`<div class="single-reward"> … </div>` 删掉或注释（`common-page.ejs` 同样处理）。

### 17.5 本项目现状（2026-11-26 已换成自己的收款码）

| 改动项 | 内容 |
| --- | --- |
| 图片文件 | `source/img/custom/donate/AliPayQR.webp`（支付宝）、`WeChanQR.webp`（微信·文章页）、`WeChanSQ.webp`（微信·打赏页） |
| 站点配置 | `_config.sakura.yml` 新增 `donate:` 段，三个键指向上面三张图 |
| 模板 | `common-article.ejs`、`common-page.ejs`、`donate.ejs` 三处改为 `url_for()`（完整外链直用，`/img/...` 自动补 `/skyblog/` 前缀） |
| 构建结果 | 文章页输出 `<img src="/skyblog/img/custom/donate/AliPayQR.webp">` |

以后换码只做一件事：**替换 `source/img/custom/donate/` 里的图片文件**（保持文件名），
然后 `hexo clean && hexo generate` + 部署即可，不用再动模板和配置。

---

## 18. 批量导入外部博客文章（84 篇实战）

2026-11-26 把 `https://aixmb.com/`（WordPress + 子比主题）全站 **84 篇**文章搬进本博客，
下面是完整可复用的做法。

### 18.1 优先用 WordPress REST API，而不是爬 HTML

| 方式 | 结果 |
| --- | --- |
| 抓文章页 HTML | 正文在 `.article-content`，图片是 `data-src` 懒加载，正则容易截断 |
| `wp-json` 接口 | 一次拿到标题/时间/分类/正文 HTML/特色图，最省事 |

```bash
# 先确认接口可用（返回 JSON 即可）
curl "https://aixmb.com/wp-json/wp/v2/posts?per_page=1&_embed=1"
```

- 正文 HTML：`content.rendered`
- 发布时间：`date`（站点本地时间，直接写进 front-matter）
- 分类/标签：`_embedded['wp:term']`
- 封面：`_embedded['wp:featuredmedia'][0].source_url`

### 18.2 转换流程（8 步）

1. 分页拉全量：`/wp-json/wp/v2/posts?per_page=100&page=N&_embed=1`
2. 清洗 HTML：删 `script/ins/style/noscript`、广告容器 `div[id^="container-"]`
3. 剔除「视频讲解」区块：原站结构是 `h2 视频讲解：` + `h2 YouTube：链接` + `h2 哔哩哔哩：链接`，
   按"标题行 + 紧跟的链接行"成组删除；正文里正常提到 YouTube 的句子不会被误删
4. 图片本地化：取 `data-src`（跳过 `thumbnail-lg.svg` 占位图），存到 `source/img/aixmb/<文章ID>/01.png…`，
   正文改写成 `/img/aixmb/<ID>/01.png`
5. HTML → Markdown：`markdownify`（`heading_style="ATX"`、`bullets="-"`）
6. 封面：特色图下载为 `cover.*`，写进 front-matter 的 `photos:`
7. 站内跳转还原：`https://站点/?golink=<base64>` 解码成真实外链（本次还原 111 处）
8. 写 front-matter：`title / date / updated / photos / categories`（原站没标签就留空）

### 18.3 产物形态

```
source/_posts/84 篇 Markdown       文件名 <文章ID>-<标题>.md（带 ID 防重名）
source/img/aixmb/<ID>/cover.*      84 张封面
source/img/aixmb/<ID>/01..NN.*     358 张正文图
```

front-matter 示例：

```yaml
---
title: "不用买服务器！Cloudflare 免费部署开源发卡系统…"
date: 2026-11-25 16:53:27
updated: 2026-11-25 18:32:17
photos:
  - /img/aixmb/1340/cover.png
categories:
  - "未分类"
---
```

### 18.4 发布前三项校验

```bash
# ① 图片引用是否都落地
python check_imgs.py        # 扫 md/HTML 里 /img/aixmb/* 引用，核对文件是否存在

# ② 构建
npx hexo clean && npx hexo generate

# ③ 敏感图排查
#    二维码/收款码 → OpenCV QRCodeDetector 多尺度（0.5/0.8/1/1.6/2.4 倍 + 大图分块）
#    联系方式类   → 用 OpenCV 把正文图拼成联系表，人眼过一遍
```

> 本次 443 张图（84 封面 + 358 正文 + 1）经二维码检测 + 联系表目视，
> 未发现二维码/收款码/微信号/手机号类图片，因此全部保留。

### 18.5 转载文章的处理约定

- 正文不保留"本文转载整理自 … 版权归原作者所有"之类尾巴（本次 84 篇已统一删除）
- 图片全部本地化，原站挂掉也不裂图
- 原站短链/跳转链还原成真实地址，读者点开直达

### 18.6 部署踩坑复盘：gh-pages 被推成源码

**现象**：线上文章还是旧内容；`gh-pages` 分支根目录出现 `_config.yml`、`source/` 等源码文件。

**原因**：`.deploy_git` 里丢了 `.git`，`hexo deploy` 的 git 命令回退到父仓库，
把**整个源码目录**提交并强推到了 `gh-pages`（也就是 §16 第 1 条的实际复现）。

**修复（临时目录 + 产物覆盖 + 强推）**：

```bash
rm -rf .deploy_git deploy_tmp
npx hexo clean && npx hexo generate

# 克隆产物分支到临时目录（不要放在 hexo-blog 里面，避免再次被父仓库 .git 接管）
git clone --depth 1 -b gh-pages https://github.com/zhixiaotx/skyblog.git /tmp/skyblog_pages
cd /tmp/skyblog_pages
find . -maxdepth 1 ! -name .git ! -name . -exec rm -rf {} +
cp -r /path/to/hexo-blog/public/* .
touch .nojekyll

git add -A
git commit -m "Site updated: $(date +'%Y-%m-%d %H:%M')"
git push -f origin gh-pages
```

**验证**：等 1~2 分钟，用带时间戳的地址绕过缓存，确认新内容已上线：

```bash
curl -s "https://zhixiaotx.github.io/skyblog/2026/11/25/文章标题/?t=$(date +%s)" | grep -c "关键内容"
```

---

## 19. 页脚署名 / 版权文字怎么改

页脚那句 `Theme Sakura by Mashiro & Hojun, Powered by Hexo, Hosted by Coding Pages`
**不是配置项**，是主题模板里写死的 HTML，改 `_config*.yml` 无效。

### 19.1 位置

| 内容 | 文件 | 行 |
| --- | --- | --- |
| 版权年 `&copy 2026` | `themes/sakura/layout/_partial/footer.ejs` | 第 19 行 |
| 主题署名/托管声明（整句） | 同上 | 第 22-25 行 |
| 两张预加载 SVG（走 honjun 的 CDN） | 同上 | 第 16-17 行（可删） |

### 19.2 本项目当前文案（2026-11-26 已改）

`footer.ejs` 里已改为：

```html
<p style="color: #666666;"></p>
...
<span style="color: #b9b9b9;">© 2026 <a href="<%- url_for('/') %>">Sky</a> · 基于 <a href="https://hexo.io/">Hexo</a> + <a href="https://github.com/honjun/hexo-theme-sakura">Sakura</a> <i class="iconfont icon-sakura rotating" style="color: #ffc0cb;display:inline-block"></i> 搭建 · 托管于 <a href="https://pages.github.com/">GitHub Pages</a>
</span>
```

页脚显示：**© 2026 Sky · 基于 Hexo + Sakura 🌸 搭建 · 托管于 GitHub Pages**

- **Sky** 是回到首页的链接：`url_for('/')` 渲染成 `/skyblog/`，子目录部署也不会错
  （用 `url_for('/')` 而不是写死 `/`，否则部署到 `/skyblog/` 子目录时点回 404）
- `Sakura` 后面那个旋转的小花花是主题自带的图标字体：
  `<i class="iconfont icon-sakura rotating" style="color:#ffc0cb;display:inline-block"></i>`，改文案时别删掉

### 19.3 想自己再改

直接编辑 `footer.ejs` 第 22-25 行那段 `<p>`，保留 `color: #b9b9b9` 和
`text-decoration: underline dotted rgba(0,0,0,.1)` 这两个样式，视觉才和页脚一致；
改完 `npx hexo clean && npx hexo generate` + 部署。

> 注意：年份是硬编码的，跨年要手动改；也可以写成
> `<%- date(new Date(), 'YYYY') %>` 自动取当前年。

---

## 20. 音乐播放器（myhkw 免插件版）

站点用的是 myhkw.cn 提供的**免插件**播放器：只要一行 `<script>`，不用装 Hexo 插件、不用改 `package.json`。

### 20.1 官方给的原始代码

```html
<script type="text/javascript" id="myhk" src="https://myhkw.cn/api/player/178355703190" key="178355703190" m="1"></script>
```

后台要求：**插到网页源码 `</body>` 之前**；若播放器不加载，再在它前面补一行 jQuery。

### 20.2 本项目落地方式

| 环节 | 位置 |
| --- | --- |
| 模板片段 | `themes/sakura/layout/_partial/music.ejs` |
| 引入位置 | `themes/sakura/layout/layout.ejs` 第 24 行（正好在 `</body>` 之前，符合官方要求） |
| 配置 | `_config.sakura.yml` 的 `music:` 段 |

`music.ejs` 内容：

```ejs
<% if (theme.music && theme.music.enable !== false) { %>
<script type="text/javascript" id="myhk"
  src="https://myhkw.cn/api/player/<%= theme.music.id %>"
  key="<%= theme.music.key || theme.music.id %>"
  m="<%= theme.music.m || '1' %>"></script>
<% } %>
```

`_config.sakura.yml`：

```yaml
music:
  enable: true
  id: "178355703190"
  key: "178355703190"
  m: "1"
```

**换歌单**：去 myhkw.cn 后台重新生成 → 把新的 `id` / `key` 填进这里即可，模板不用动。
**临时关掉**：`enable: false`。

### 20.3 两个注意点

1. **旧播放器已删除**：原先的 `_partial/aplayer.ejs`（meting API + APlayer）已移除并替换为本方案，
   避免两个播放器同时出现、也避免 meting 接口失效导致页面报错。
2. **不需要额外加载 jQuery**：主题的 `js/lib.min.js` 已内置 jQuery（已确认），
   只有在换主题/裁剪脚本后播放器不出现时，才在 `music.ejs` 的 script 前加：

   ```html
   <script type="text/javascript" src="https://myhkw.cn/player/js/jquery.min.js"></script>
   ```

### 20.4 只在首页显示（可选）

把 `layout.ejs` 第 24 行改成：

```ejs
<% if (is_home()) { %><%- partial('_partial/music') %><% } %>
```

### 20.5 自检

```bash
# 播放器脚本接口可用（返回 application/javascript 即正常）
curl -I "https://myhkw.cn/api/player/178355703190"

# 构建产物里应有 myhk 脚本，且不再有旧 APlayer/meting 残留
grep -c "myhkw.cn" public/index.html      # ≥1
grep -c "meting\|APlayer.min.js" public/index.html   # 0
```

---

## 21. 首页头像与头像下方的社交链接

首页头部中间那张圆形头像、以及下面那一排小图标，都由主题配置控制，不用改模板。

### 21.1 头像

| 环节 | 位置 |
| --- | --- |
| 配置 | `_config.sakura.yml` 的 `avatar:` |
| 图片 | 放 `source/img/custom/avatar.jpg`（正方形，建议 ≥200×200） |
| 渲染 | `themes/sakura/layout/_partial/headertop.ejs` 第 6-16 行，圆形裁切由 CSS `.header-tou img` 负责 |

换头像三步：

1. 图片放到 `source/img/custom/avatar.jpg`
2. `_config.sakura.yml` 改 `avatar: /img/custom/avatar.jpg`（以 `/` 开头走 `url_for`，子目录部署不会裂图）
3. `npx hexo clean && npx hexo generate`

也支持直接写外链：`avatar: https://example.com/avatar.jpg`。
当前用的是 `/img/favicon.png`（站点图标兼作头像），所以看着偏小。

### 21.2 头像下方的社交链接

- 配置：`_config.sakura.yml` 的 `social:` 段
- 模板：`headertop.ejs` 第 24-43 行
- 每项字段：`url`（点击去哪）、`img`（图标）、可选 `qrcode`（鼠标悬停弹二维码）

```yaml
social:
  github: {url: https://github.com/zhixiaotx, img: /img/social/github.png}
  sina: {url: https://weibo.com/, img: /img/social/sina.png}
  wangyiyun: {url: https://music.163.com/, img: /img/social/wangyiyun.png}
  zhihu: {url: https://www.zhihu.com/, img: /img/social/zhihu.png}
  email: {url: mailto:liuliu19901110@gmail.com, img: /img/social/email.svg}
  wechat: {url: https://weixin.qq.com/, img: /img/social/wechat.png}
  wechat2: {url: https://mp.weixin.qq.com/, img: /img/social/wechat.png}
```

顺序就是显示顺序（当前 7 个：github / 微博 / 网易云 / 知乎 / 邮箱 / 微信 / 微信公众平台）。
除 GitHub 和邮箱是本项目的真实地址外，其余 5 个填的是**各平台官网的官方地址**做占位，
要换成自己的主页只需改对应 `url`。

### 21.3 两个坑（重要）

1. **旧图标删不掉**：Hexo 会把你写的 `social` 与 `themes/sakura/_config.yml` 里的 `social` **深合并**，
   站点配置里没覆盖到的键会继续显示。所以「增删图标」必须两边同步改
   —— 本项目主题 `_config.yml` 与 `_config.sakura.yml` 已保持一致：
   保留原主题 7 个图标，但把原作者的个人链接（mashirozx 的微博、Hojun 的 QQ 等）全部换成各平台官方地址。
2. **图标图片走 CDN**：`headertop.ejs` 里写的是 `(theme.cdn || '') + img`，**没有** `url_for`，
   所以 `img: /img/social/github.png` 实际加载的是
   `https://cdn.jsdelivr.net/gh/honjun/cdn@1.6/img/social/github.png`。
   想用自己的图标：要么 `img` 写成完整外链，要么把模板这几处改成 `url_for()` 并把图片放进 `source/img/social/`。

### 21.4 微信 / 公众号的悬停二维码

`wechat`（微信）和 `wechat2`（公众号）两个图标带 `qrcode` 字段，鼠标悬停会弹出二维码。

| 环节 | 位置 |
| --- | --- |
| 配置 | `_config.sakura.yml` 的 `social.wechat.qrcode` / `social.wechat2.qrcode` |
| 图片 | `source/img/custom/wechat.webp`、`source/img/custom/wechat-mp.webp` |
| 模板 | `headertop.ejs` 第 31-34 行（已改为 `url_for()`，本地图才能生效） |

```yaml
wechat: {url: https://weixin.qq.com/, img: /img/social/wechat.png, qrcode: /img/custom/wechat.webp}
wechat2: {url: https://mp.weixin.qq.com/, img: /img/social/wechat.png, qrcode: /img/custom/wechat-mp.webp}
```

换二维码只有两种做法：

1. **替换文件**（推荐）：把新二维码覆盖到 `source/img/custom/wechat.webp` 和 `wechat-mp.webp`，文件名保持不变
2. **改配置**：把 `qrcode` 改成完整外链，例如 `qrcode: https://example.com/my-qr.png`

> 注意：`qrcode` 原来走的是 `(theme.cdn || '') + qrcode`，写本地路径会拼成 jsdelivr 上原作者的图；
> 本项目已把这处改成 `url_for()`，所以 `/img/...` 本地路径能正常工作。
> 主题自带的图标 `img:` 仍然走 CDN，两处行为不一样，别混。
>
> 当前这两张图是**临时占位**（复用微信赞赏码），换成你自己的微信/公众号码即可。

### 21.5 手机端

移动端用的是 `msocial:`（Font Awesome 图标，不需要图片），同样受深合并影响。
本项目当前为 github / 微博 / QQ / 邮箱，链接同样是各平台官方地址，改 `_config.sakura.yml` 的 `msocial:` 即可。

### 21.6 自检

```bash
grep -c "img/social/" public/index.html          # 当前项目应为 7
grep -o 'img/custom/wechat[^"]*' public/index.html   # 应为 wechat.webp 与 wechat-mp.webp
```

---

## 22. 导航栏站名左边加头像

顶部导航栏左侧那个「Sky」是纯文字 logo（`.sakurasono` 前缀 + `.shironeko` 站名），
现在在它左边加了一个圆形头像，**复用的就是首页中间那个头像**，所以换头像只改一处。

### 22.1 位置

| 环节 | 文件 / 行 |
| --- | --- |
| 结构 | `themes/sakura/layout/_partial/header.ejs` 第 6-13 行（`.logolink > a` 内） |
| 头像来源 | `_config.sakura.yml` 的 `avatar:`（与首页头像同一项） |
| 样式 | 内联在 `<img>` 上，改 `width/height/border-radius/margin-right` 即可 |

### 22.2 现在的写法

```ejs
<a href="<%- url_for('/') %>" style="display:inline-flex;align-items:center;gap:8px;float:left">
  <% var _navAvatar = theme.avatar || ''; %>
  <% var _navAvatarSrc = /^https?:\/\//.test(_navAvatar) || _navAvatar.indexOf('//') === 0 ? _navAvatar : (_navAvatar.indexOf('/') === 0 ? url_for(_navAvatar) : url_for((theme.cdn || '') + _navAvatar)); %>
  <img class="site-logo-avatar" src="<%- _navAvatarSrc %>" alt="<%= theme.siteName %>"
       style="width:30px;height:30px;border-radius:50%;object-fit:cover;margin:0;flex:0 0 auto;opacity:1;box-shadow:0 0 4px rgba(0,0,0,.15)">
  <span class="sakurasono"><%= theme.prefixName %></span>
  <span class="shironeko"><%= theme.siteName %></span>
</a>
```

**为什么用 `inline-flex` 而不是 `vertical-align:middle`**：导航栏的 `.logolink a` 设了
`height:56px; line-height:56px`，同时主题还有一条 `.site-title img { height:40px; margin-top:17px; opacity:.75 }`
会把头像顶偏、变淡。改成父级 `display:inline-flex; align-items:center` 后由 flex 居中对齐，
再用内联 `margin:0`、`opacity:1` 覆盖掉主题的旧规则，头像和「Sky」就齐平了。

三种 `avatar` 写法都兼容：

- `https://.../a.jpg`（完整外链）→ 直接用
- `/img/favicon.png`（以 `/` 开头）→ 走 `url_for`，自动补 `/skyblog/` 前缀
- `avatar.jpg`（相对路径）→ 拼主题 `cdn`

### 22.3 想让导航栏用另一张图

把上面 `<img>` 的 `src` 直接换成固定路径即可，例如：

```ejs
<img class="site-logo-avatar" src="<%- url_for('/img/custom/logo.png') %>" ...>
```

### 22.4 想调大小 / 去掉

- 大小：改 `width:30px;height:30px`（建议 24–36px；容器是 `inline-flex`，会随高度自动居中）
- 间距：改父级 `<a>` 的 `gap:8px`
- 去掉：把 `<img ...>` 那一行删掉；父级的 `inline-flex` 留着也不影响原来的文字 logo

### 22.5 自检

```bash
grep -o 'site-logo-avatar[^>]*' public/index.html | head -1
# 期望看到 src="/skyblog/img/favicon.png"
```

---

## 23. 去掉标题后面的 ¶ 符号

每篇文章的 `<h2>` 标题末尾都会多出一个红色 `¶`（如「十二、项目地址 ¶」「最后总结 ¶」）。

**它不是正文内容**：Markdown 源文件里搜不到这个字符（`grep ¶ source/_posts/*.md` = 0），
是主题 CSS 的伪元素画出来的：

```css
.entry-content h2:after {
    content:"\00B6";   /* ¶ */
    position:absolute;
    color:#ff6d6d;
    ...
}
.serif .entry-content h2:after { content:"\00B6"; ... }   /* 衬线字体的另一份 */
```

所以改文章没用，只能改样式。

### 23.1 位置与改法

| 环节 | 文件 / 行 |
| --- | --- |
| 规则 | `themes/sakura/source/css/style.css` 第 2103-2118 行（两条：普通 + `.serif` 变体） |
| 改法 | 把 `content:"\00B6";` 改成 `content:none;` |

本项目已把两处都改成 `content:none`，生成后的 `public/css/style.css` 里 `00B6` 出现次数为 0。

### 23.2 顺带说明

- 同一份 CSS 里 `<h3>` 后面还有个 `#`（`.entry-content h3:after { content:"#" }`），
  这次没动；不想要的话同样改成 `content:none`
- 这些样式是**纯 CSS 文件**（不是 `.styl`），直接改 `themes/sakura/source/css/style.css` 即可，
  不用管 stylus 编译

### 23.3 自检

```bash
grep -c '00B6' public/css/style.css     # 应为 0
grep -o 'h2:after {[^}]*}' public/css/style.css | head -2   # 应看到 content:none
```

---

## 24. 关掉头部背景视频（不自动播放）

**现象**：打开首页或任意文章，头部会自动加载并播放背景视频（`Unbroken.mp4`），
中间还会出现「正在载入视频 ...」的提示、右侧有个播放按钮。

### 24.1 它从哪来

| 环节 | 位置 |
| --- | --- |
| 视频地址配置 | `themes/sakura/_config.yml` 的 `movies: {url, name}` |
| 注入到页面 | `themes/sakura/layout/_partial/footer.ejs` 第 47-51 行 → `var Poi.movies = {url, name, live}`（桌面端 `live:"open"`） |
| 播放逻辑 | `themes/sakura/source/js/sakura-app.js`：`Siren.addsource()` 把 `Poi.movies.url/name` 写进 `#bgvideo` 的 `src` → `Siren.splay()` → `s.play()` |
| DOM | `themes/sakura/layout/_partial/headertop.ejs` 的 `#video-container`（含 `#video-btn`、`.video-stu`） |

也就是说：**这不是文章里的视频，是主题自带的"电影背景"功能**，跟 Markdown 内容无关。

### 24.2 本项目的关停改动（三处）

1. `_config.sakura.yml` 里把视频清空：

   ```yaml
   movies:
     url: ""
     name: ""
   ```

2. `headertop.ejs` 第 52-57 行：`#video-container` 加 `display:none`，
   `preload="auto"` 改 `preload="none"`，并删掉 `#video-btn` / `#video-add` / `.video-stu`
   —— 只保留一个空的 `<video id="bgvideo">`，否则 `sakura-app.js` 里 `$('#bgvideo')[0]` 取不到会报错

3. `sakura-app.js` 加卫语句：

   ```js
   addsource: function () {
     if (!Poi.movies || !Poi.movies.name) return
     ...
   }
   liveplay: function () {
     if (!s) return
     ...
   }
   ```

**效果**：浏览器不再请求 `Unbroken.mp4`，头部只显示壁纸大图，也不会出现「正在载入视频」。

### 24.3 想恢复背景视频

把 `url`（视频所在目录）和 `name`（文件名，多个用逗号分隔）填回去，
再去掉 `headertop.ejs` 里 `#video-container` 的 `display:none`、把 `preload` 改回 `auto` 即可。

### 24.4 自检

```bash
grep -o '"movies":{[^}]*}' public/index.html     # 应为 url/name 空
grep -c 'preload="none"' public/index.html       # ≥1
grep -c 'id="video-btn"' public/index.html       # 0
```

> 注意：左下角那个是**音乐播放器**（myhkw），不是视频；它的播放开关在 myhkw.cn 后台设置里。

---

## 25. 部署到 Trae 站点（traesite.cn）

线上地址：<https://skyblog.traesite.cn>（所有人可见）。

### 25.1 和 GitHub Pages 的差别

| 项目 | GitHub Pages | Trae 站点 |
| --- | --- | --- |
| 站点路径 | 子目录 `/skyblog/` | 站点根 `/` |
| 静态资源 | 直接放在 `public/` | 改走版本化挂载 `/_assets/<version>/` |
| 发布形态 | 全部静态文件 | HTML 由 Node 20 进程直出，图片/JS/CSS 等独立上传 |

同一份源码要同时兼容两种环境，靠的是**构建时改 `url` / `root`、打包时改资源前缀**，仓库里的源码不用动。

### 25.2 构建

```bash
# 用临时配置覆盖，不改 _config.yml，GitHub Pages 的子目录部署不受影响
cat > /tmp/trae-deploy-config.yml <<'EOF'
url: https://skyblog.traesite.cn
root: /
EOF

npx hexo clean
npx hexo generate --config "_config.yml,/tmp/trae-deploy-config.yml"
```

`public/` 里的文件数会到 600+，超出静态直发阈值后由部署侧自动转成「Node 20 静态服务 + 版本化资源挂载」，无需手动改项目。

### 25.3 打包时做的两处 URL 适配

1. 文章正文里硬编码的 `/skyblog/img/...` 前缀去掉 `/skyblog`，改为根路径（正文里的绝对路径不受 `root` 影响，只能在这一步改）；
2. HTML 里的资源地址统一加 `/_assets/<version>/` 前缀，**页面跳转链接保持业务路径**（`/archives/`、`/2026/11/25/...` 之类不动）。

### 25.4 自检

```bash
curl -sI https://skyblog.traesite.cn/ | head -1                  # 期望 200
curl -s  https://skyblog.traesite.cn/ | grep -c '/skyblog/'      # 期望 0
curl -sI https://skyblog.traesite.cn/img/favicon.png | head -1   # 307 → 200（旧路径兼容跳转）
```

## 26. 首页社交图标改成站内 SVG

现象：首页描述条下面那排社交图标只有邮箱正常，其余全是破图。

原因：`headertop.ejs` 把图标路径无脑拼到主题 CDN 上（`(theme.cdn || '') + theme.social[i].img`），而 CDN 上的 `img/social/*.png` 实际取不到；`email.svg` 恰好能取到，所以只有它显示。

改法（三处一起改，缺一不可）：

1. 图标放进 `source/img/social/`：`github.svg`、`sina.svg`、`wangyiyun.svg`、`zhihu.svg`、`wechat.svg`、`email.svg`（Font Awesome 免费品牌图标，`fill` 改为 `#ffffff` 适配深色条）；
2. `_config.sakura.yml` 里 `social.*.img` 指向 `/img/social/*.svg`；
3. `headertop.ejs` 增加路径判定：以 `/` 开头走 `url_for()`（站内），以 `http(s)://` 或 `//` 开头原样输出，其余才拼主题 CDN。

### 26.1 自检

```bash
grep -o 'src="[^"]*/img/social/[^"]*"' public/index.html
grep -c 'cdn.jsdelivr.net/gh/honjun/cdn@1.6/img/social' public/index.html   # 期望 0
```

## 27. 标签页 / 分类页封面占位修复

现象：`/tags/xxx/`、`/categories/xxx/` 里出现 `<img data-src="github.img">` 这种地址，必然 404。

原因：`tag.ejs` / `category.ejs` 用 `__(page.tag + '.img')` 取封面，语言文件里没有这个 key 时 Hexo 会**原样返回 key**，于是拼出了 `xxx.img`。

改法：取到的值和 key 相同时视为「没有配置封面」，回退到默认封面图（`https://view.moezx.cc/images/2017/12/03/writing.jpg`）。

## 28. 看板娘（Live2D 猫咪）

之前右下角没有猫：主题里只留了看板娘的 CSS，没有任何加载脚本。

现在的结构：

| 位置 | 内容 |
| --- | --- |
| `source/live2d/lib/` | `L2Dwidget.min.js` + `L2Dwidget.0.min.js`（后者是动态 chunk，靠 `currentScript` 定位，必须和前者同目录） |
| `source/live2d/models/tororo/` | 白猫 tororo 模型（moc / 贴图 / mtn 动作，约 730 KB） |
| `_partial/footer.ejs` 末尾 | 初始化代码：右下角、150×300、悬停变淡、手机端不显示 |

全部是站内资源，不依赖任何第三方 CDN。

### 28.1 换模型 / 改位置

把模型目录整体放进 `source/live2d/models/<名字>/`，改 `footer.ejs` 里的 `jsonPath`；大小改 `display.width / height`，左右位置改 `display.position`。

### 28.2 自检

```bash
ls public/live2d/lib public/live2d/models/tororo
grep -o "jsonPath: '[^']*'" public/index.html
```

页面加载后按 F12 打开控制台执行 `document.querySelector('#live2dcanvas')`，能取到 canvas 即为正常。

## 29. 作者小头像裂图（友人帐 / 关于 / 打赏 / 手机侧边栏）

现象：`/about/` 正文页的作者小头像、`/links/`、`/donate/` 的作者卡片、手机端抽屉里的头像全部裂图，
请求的地址是 `https://cdn.jsdelivr.net/gh/honjun/cdn@1.6/img/favicon.png`（CDN 上根本没有这个文件）。

根因和第 26 节一样：这几个模板把 `theme.avatar`（值已经是站内的 `/img/favicon.png`）又拼了一次主题 CDN，
`url_for()` 对绝对地址原样返回，于是拼出了一个不存在的 CDN 地址。

涉及 4 个模板，统一改成同一段判定：

| 文件 | 位置 |
| --- | --- |
| `layout/links.ejs` | `section.author-profile` 作者卡片 |
| `layout/donate.ejs` | `section.author-profile` 作者卡片 |
| `layout/_widget/common-page.ejs` | 普通页面的作者信息块 |
| `layout/_partial/mheader.ejs` | 手机端抽屉头像 |

```ejs
<% var _avatar = theme.avatar || ''; %>
<% var _avatarSrc = /^https?:\/\//.test(_avatar) || _avatar.indexOf('//') === 0
     ? _avatar
     : (_avatar.indexOf('/') === 0 ? url_for(_avatar) : url_for((theme.cdn || '') + _avatar)); %>
<img src="<%- _avatarSrc %>" ...>
```

判定顺序和 `headertop.ejs` / `header.ejs` 保持一致：`http(s)://` 或 `//` 开头 → 原样；`/` 开头 → 站内 `url_for`；其余 → 拼主题 CDN。

### 29.1 自检

```bash
# 构建产物里不应再出现 CDN 头像地址
grep -rc 'honjun/cdn@1.6/img/favicon.png' public --include=*.html | grep -v ':0' || echo "clean"

# 作者卡片头像应为站内路径
grep -o 'class="profile gravatar"><img src="[^"]*"' public/about/index.html
```

> 另外：仓库原来只有 `about / categories / tags` 三个页面，导航栏里的「友人帐」等入口没有对应页面，
> 点开是 404。已在第 30 节补上 `links` 和 `donate` 两个页面。

## 30. 友人帐 / 打赏 页面

导航栏「友人帐」原来指向 `/links/`，但仓库里没有这个页面，点开 404。现在两个页面都补上了：

| 页面 | 文件 | layout |
| --- | --- | --- |
| `/links/` 友人帐 | `source/links/index.md` | `links` |
| `/donate/` 打赏 | `source/donate/index.md` | `donate` |

### 30.1 友人帐：友链写在 front-matter

`layout/links.ejs` 只认 `page.links`，正文写什么都不显示，所以友链要维护在 front-matter：

```yaml
---
title: 友人帐
layout: links
photos: /img/wallpaper/country-cottage.webp   # 页头大图
links:
  - group: 本站          # 分组名
    desc: 自己的站点      # 可选，分组说明
    items:
      - name: Sky 的博客
        url: https://skyblog.traesite.cn
        img: /img/favicon.png              # 头像，建议用站内路径
        desc: 记录技术与思考
---
```

`img` 加载失败时主题会自动换成默认头像（模板里 `onerror="imgError(this,1)"`）。

### 30.2 打赏：收款码来自主题配置

`layout/donate.ejs` 读的是 `_config.sakura.yml` 里的 `donate`：

```yaml
donate:
  paypal: "javascript:;"                      # 关键：不填会用主题作者的 PayPal 收款链接
  alipay: /img/custom/donate/AliPayQR.webp
  wechat: /img/custom/donate/WeChanQR.webp
  wechatSQ: /img/custom/donate/WeChanSQ.webp
```

> 换收款码只换 `source/img/custom/donate/` 下的图片文件即可，文件名不用改。

### 30.3 自检

```bash
ls public/links/index.html public/donate/index.html
curl -sI https://skyblog.traesite.cn/links/  | head -1     # 200
curl -sI https://skyblog.traesite.cn/donate/ | head -1     # 200
```

---

## 31. 看板娘挪到左侧 + 社交图标改回品牌色

### 31.1 问题

1. Live2D 看板娘默认在右下角，和音乐播放器（`#myhkplayer`，左下 300×181）挤在一起、互相遮挡。
2. 首页 banner 中间那排社交图标（`.top-social_v2`）全是白色剪影，看不出是哪个平台。

### 31.2 看板娘：改 `position` 与 `vOffset`

`themes/sakura/layout/_partial/footer.ejs`：

```ejs
display: { superSample: 2, width: 150, height: 300, position: 'left', hOffset: 0, vOffset: 240 },
```

| 参数 | 原值 | 新值 | 作用 |
|---|---|---|---|
| `position` | `'right'` | `'left'` | 挪到页面左侧 |
| `vOffset` | `-20` | `240` | 往上抬 240px，避开左下 300×181 的播放器 |

**关键坑：不能只靠 CSS 覆盖。** L2Dwidget 会给自己注入内联样式 `bottom: -20px`（值就是 `vOffset`），实测在样式表里写 `#live2d-widget{bottom:240px !important}` 在这套脚本里并不生效，最稳的做法是**直接改 `vOffset`**，让脚本自己算出正确的 `bottom`。

（`style.css` 末尾也留了一条同名规则做双保险，注释已标明。）

### 31.3 社交图标：把 SVG 的 `fill` 从白改回品牌色

`source/img/social/*.svg` 六个文件原来都是 `fill="#ffffff"`，逐个替换：

| 文件 | 颜色 | 平台 |
|---|---|---|
| `github.svg` | `#181717` | GitHub |
| `sina.svg` | `#E6162D` | 新浪微博 |
| `wangyiyun.svg` | `#C20C0C` | 网易云音乐 |
| `zhihu.svg` | `#0084FF` | 知乎 |
| `email.svg` | `#D44638` | 邮箱 |
| `wechat.svg` | `#07C160` | 微信 / 公众号 |

图标仍是本地 SVG（跟着 `url_for()` 走 `/skyblog/img/social/`），没有换回主题的 honjun CDN，避免裂图。

### 31.4 自检

```bash
# 看板娘配置
grep -o "position: 'left'\|vOffset: 240" public/index.html

# 社交图标不再是白色
grep -o 'fill="#[0-9A-Fa-f]*"' public/img/social/*.svg
# → #181717 / #E6162D / #C20C0C / #0084FF / #D44638 / #07C160
```

### 31.5 线上验证

```js
// 看板娘在左侧、抬到播放器上方
const w = document.querySelector('#live2d-widget').getBoundingClientRect();
// { x: 0, y: 170, width: 150, height: 300 }  → left=0，bottom=240
```

音乐播放器 `#myhkplayer` 占底部 40–221px（300×181），看板娘从 240px 起，**两者不再重叠**。

---

## 32. 移动端页脚与电脑端署名统一

### 32.1 问题

电脑端页脚是改过的：

```
© 2026 Sky · 基于 Hexo + Sakura 🌸 搭建 · 托管于 GitHub Pages
```

但手机端点开侧边菜单，最底下还是主题自带的硬编码文字：

```
© 2019 hexo-sakura
```

两处分别写在不同的模板里，改电脑端时漏了移动端。

### 32.2 两处文件

| 位置 | 模板 | 说明 |
|---|---|---|
| 电脑端 | `themes/sakura/layout/_partial/footer.ejs` 第 23 行 | `.footer-device` 里的署名 |
| 移动端 | `themes/sakura/layout/_partial/mheader.ejs` 第 38 行 | `#mo-nav` 抽屉底部，原来是写死的 `&copy 2019 hexo-sakura` |

`mheader.ejs` 那段原来是：

```ejs
<p style="text-align: center; font-size: 13px; color: #b9b9b9;">&copy 2019 hexo-sakura</p>
```

### 32.3 改法

把移动端那行换成和电脑端一致的内容（保留移动端的小字号与居中，加了左右内边距防止贴边）：

```ejs
<p style="text-align: center; font-size: 13px; color: #b9b9b9; padding: 0 12px 10px; line-height: 1.8;">
  <span style="color: #b9b9b9;">© 2026
    <a href="<%- url_for('/') %>" style="color: #b9b9b9; text-decoration: underline dotted rgba(0, 0, 0, .1);">Sky</a>
    · 基于 <a href="https://hexo.io/" target="_blank" ...>Hexo</a>
    + <a href="https://github.com/honjun/hexo-theme-sakura" target="_blank" ...>Sakura</a>
    <i class="iconfont icon-sakura rotating" style="color: #ffc0cb; display: inline-block;"></i>
    搭建 · 托管于 <a href="https://pages.github.com/" target="_blank" ...>GitHub Pages</a>
  </span>
</p>
```

要点：

- 站名 `Sky` 用 `url_for('/')` 回首页，**必须带 `<%- %>`**（不转义），否则子目录 `/skyblog/` 下链接会拼错
- 旋转小花花 `<i class="iconfont icon-sakura rotating">` 一起搬过来，两边视觉一致
- 颜色统一 `#b9b9b9`，和电脑端同色

### 32.4 自检

```bash
# 旧文案不该再出现
grep -rc '2019 hexo-sakura' public/ | grep -v ':0'   # 应无输出

# 移动端抽屉里也有完整署名
grep -o 'id="mo-nav"' public/index.html
grep -c '托管于' public/index.html                     # ≥2（电脑端 + 移动端）

# EJS 占位符别漏渲染成字符串
grep -c '&lt;%-' public/index.html                    # 0
```

### 32.5 备忘

下次改页脚署名，两处一起改：

```
themes/sakura/layout/_partial/footer.ejs    # 电脑端
themes/sakura/layout/_partial/mheader.ejs   # 移动端（#mo-nav 抽屉底部）
```

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