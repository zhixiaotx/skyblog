---
title: 图集
layout: default
photos: /img/wallpaper/beach-sailboat.webp
---

存下来的图。都是站内壁纸，不依赖外链，换图只要替换 `source/img/wallpaper/` 里对应的文件。

## 海边帆船

![海边帆船](../../img/wallpaper/beach-sailboat.webp)

## 城市夜色

![城市夜景](../../img/wallpaper/city-night.webp)

## 乡村小屋

![乡村小屋](../../img/wallpaper/country-cottage.webp)

## 吊床

![吊床](../../img/wallpaper/hammock.webp)

---

> **为什么图片路径写 `../../img/...` 而不是 `/img/...`**
>
> 这个页面生成在 `/list/gallery/`，`../../` 正好回到站点根目录。
> - 部署在 `github.io/skyblog/` 时：`/skyblog/list/gallery/` + `../../` → `/skyblog/img/...` ✅
> - 绑到自定义域名根目录时：`/list/gallery/` + `../../` → `/img/...` ✅
>
> 写成 `/img/...` 的话，子目录部署会丢 `/skyblog` 前缀，图就裂了。
