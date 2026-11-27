---
title: 留言板
layout: default
photos: /img/wallpaper/country-cottage.webp
---

> 占位页。评论系统还没开，所以这里现在是空的。

## 怎么让它真能留言

`_config.sakura.yml` 里现在是：

```yaml
# 评论系统：暂不启用（如需可配置 Valine / Waline）
valine: false
```

二选一配好就生效：

**方案 A：Valine（LeanCloud）**

```yaml
valine: true
valine_appid: 你的AppID      # LeanCloud 国际版 → 设置 → 应用凭证
valine_appkey: 你的AppKey
valine_placeholder: 随便说点什么吧...
```

**方案 B：Waline（可自托管）**

```yaml
waline:
  enable: true
  serverURL: https://你的waline实例
```

改完 `npx hexo clean && npx hexo generate` 重新部署。

## 先在这里找我

- GitHub：[@zhixiaotx](https://github.com/zhixiaotx)
- 邮箱：liuliu19901110@gmail.com

---

> 提示：这一页用的是默认 `page` 布局，评论组件的挂载点在主题的
> `layout/_partial/comment.ejs` 里，需要主题开启评论才会渲染出来。
