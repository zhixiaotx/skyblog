---
title: 留言板
layout: default
photos: /img/wallpaper/country-cottage.webp
---

随便说点什么吧，不用客气。

## 怎么留言

留言功能走评论系统。当前 `_config.sakura.yml` 里是：

```yaml
# 评论系统：暂不启用（如需可配置 Valine / Waline）
valine: false
```

所以这一页暂时是空白的留言区。想让它真的能留言，二选一：

### 方案 A：Valine（LeanCloud）

1. 去 [LeanCloud](https://console.leancloud.app/) 建一个国际版应用
2. 在「设置 → 应用凭证」拿到 `AppID` / `AppKey`
3. 填进 `_config.sakura.yml`：

```yaml
valine: true
valine_appid: 你的AppID
valine_appkey: 你的AppKey
valine_placeholder: 随便说点什么吧...
```

### 方案 B：Waline（可自托管）

```yaml
waline:
  enable: true
  serverURL: https://你的waline实例
```

改完 `npx hexo clean && npx hexo generate` 重新部署即可。

## 先在这里找我

- GitHub：[@zhixiaotx](https://github.com/zhixiaotx)
- 邮箱：liuliu19901110@gmail.com

---

> 提示：这一页用的是默认 `page` 布局，评论组件的挂载点在主题的
> `layout/_partial/comment.ejs` 里，需要主题开启评论才会渲染出来。
