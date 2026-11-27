---
title: 友人帐
layout: links
photos: /img/wallpaper/country-cottage.webp
# 友链分组：group 分组名，desc 可选说明；每组 items 里填 name / url / img / desc
# img 建议用站内图片（以 / 开头），也可以用完整 https 地址；加载失败会走主题默认头像
links:
  - group: 本站
    desc: 自己的站点
    items:
      - name: Sky 的博客
        # url 写 home 时由 links.ejs 渲染成相对路径 ../，
        # 这样挂在 github.io/skyblog/ 还是任何自定义域名根目录，点进来都回首页
        url: home
        img: /img/favicon.png
        desc: 记录技术与思考
  - group: 常用
    items:
      - name: Hexo
        url: https://hexo.io
        img: /img/favicon.png
        desc: 快速、简洁且高效的博客框架
      - name: Sakura
        url: https://github.com/honjun/hexo-theme-sakura
        img: /img/favicon.png
        desc: 本项目使用的 Sakura 主题
---

友链列表见页面正文，正文内容由主题模板渲染，这里只维护 front-matter 里的 `links`。
