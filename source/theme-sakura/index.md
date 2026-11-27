---
title: 主题
layout: default
photos: /img/wallpaper/anime-scene.webp
---

这篇文章说说这个博客用的主题：**Sakura**。

## 为什么选它

- 首页那张大图 + 圆形头像 + 社交图标的排版，第一眼就对
- 自带「开始菜单」（StartDash）、标签页、分类页，不用自己写
- 主题本身是 EJS + 一份大 `style.css`，改起来比编译型主题直接得多

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 主题名 | Sakura（二次元风格） |
| 上游仓库 | [honjun/hexo-theme-sakura](https://github.com/honjun/hexo-theme-sakura) |
| 框架 | Hexo 7 |
| 模板语言 | EJS |
| 部署 | GitHub Pages（`gh-pages` 分支） |

## 本站对它做过哪些改动

改动都记在 README 里，按编号排列，这里挑几条影响最大的：

1. **头部背景视频停用** —— 自动播放的视频太吵也太拖加载，直接去掉
2. **Banner 固定高度 550px** —— 主题原本 `height: 0` 靠 JS 展开，停用视频后就塌了
3. **标题后的 ¶ 去掉** —— `h2:after` 的 `content` 改成 `none`
4. **社交图标本地化** —— 从 honjun CDN 换成本地 SVG，再改成品牌色
5. **看板娘挪到左侧** —— 避免和音乐播放器重叠
6. **页脚署名统一** —— 电脑端和移动端抽屉都用同一句

## 配置是怎么覆盖的

关键点：`hexo-blog/_config.sakura.yml` 会**深合并**覆盖主题自己的 `_config.yml`。
同名键覆盖、缺失的继承。所以想删掉主题里某个数组项，光改站点配置不够，
得连主题那份一起改——这点在配社交图标时踩过。

## 想换主题的话

Hexo 换主题只要三步：把主题目录放进 `themes/`，改根 `_config.yml` 的 `theme:`，
再按新主题的要求补齐配置。但注意我们的自定义改动全在 `themes/sakura/` 里，
换主题等于那些改动全部失效，得重新来一遍。

---

→ 返回 [关于我](../about/)
