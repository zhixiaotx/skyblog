# 我的技术博客 (Hexo + Butterfly)

基于 [Hexo](https://hexo.io/) 与 [Butterfly](https://github.com/jerryc127/hexo-theme-butterfly) 主题的个人博客。

## 线上地址

**https://zhixiaotx.github.io/skyblog/**

## 仓库分支结构

| 分支 | 内容 | 说明 |
| --- | --- | --- |
| `main` | Hexo 源码 | 主题配置、文章源文件、依赖清单 |
| `gh-pages` | 构建产物 | 由 `hexo d` 自动推送，GitHub Pages 实际对外提供的内容 |
| `source` | 源码备份 | 与 `main` 同步的备份分支 |

> GitHub Pages 的 Source 已设为 `gh-pages` 分支（根目录 `/`）。

## 本地运行

```bash
cd hexo-blog
npm install          # 首次或新增依赖后
npx hexo s           # 启动本地预览，默认 http://localhost:4000
```

## 写新文章

```bash
npx hexo new "文章标题"      # 在 source/_posts/ 生成 Markdown
npx hexo new page about     # 生成独立页面（about 已存在）
```

编辑 `source/_posts/*.md`，Front-matter 支持 `title / date / tags / categories` 等字段。

## 构建与部署

```bash
npx hexo clean        # 可选：清理 public/ 缓存
npx hexo d -g         # 生成静态文件并部署到 gh-pages
```

部署配置见根目录 `_config.yml` 的 `deploy` 段（已指向 `zhixiaotx/skyblog` 的 `gh-pages`）。

## 常用配置位置

- 站点信息（标题/语言/URL/菜单）：`_config.yml`
- 主题外观（社交链接/头像/搜索/配色）：`_config.butterfly.yml`
- 文章与页面：`source/_posts/`、`source/about/`
- 主题文件：`themes/butterfly/`（如需深度定制请复制配置到 `_config.butterfly.yml` 覆盖，避免直接改主题文件）

## 目录结构

```
hexo-blog/
├─ _config.yml            # Hexo 主配置
├─ _config.butterfly.yml  # Butterfly 主题覆盖配置
├─ source/                # 文章与页面源文件
├─ themes/butterfly/      # Butterfly 主题
├─ scaffolds/             # 文章模板
└─ package.json           # 依赖
```

## 注意事项

- 部署需要本地 `git` 已登录 GitHub（`gh auth login`）。本机已通过 `gh` 凭证登录账号 `zhixiaotx`。
- 修改站点 `url`/`root` 后请重新 `hexo d -g`，否则静态资源路径可能出错。
