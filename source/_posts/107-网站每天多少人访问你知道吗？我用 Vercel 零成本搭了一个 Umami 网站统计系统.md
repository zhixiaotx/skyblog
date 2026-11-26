---
title: "网站每天多少人访问你知道吗？我用 Vercel 零成本搭了一个 Umami 网站统计系统"
date: 2026-07-02 11:17:55
updated: 2026-07-16 19:54:18
photos:
  - /img/aixmb/107/cover.webp
categories:
  - "网站搭建"
source_url: https://aixmb.com/107.html
---

很多人搭好了网站，却不知道：

❌ 每天有多少访客  
❌ 用户从哪里来  
❌ 哪个页面最受欢迎  
❌ 哪些内容真正有人看

如果你也有这些困扰，那么今天这个开源神器值得收藏。

📦 项目名称：Umami

它是一款开源、轻量、隐私优先的网站统计工具，可以理解为 Google Analytics 的简洁替代方案。

---

## **✨ Umami 有什么优势？**

✅ 开源免费

✅ 界面简洁易懂

✅ 实时访问统计

✅ 访客来源分析

✅ 热门页面排行

✅ 注重用户隐私

✅ 部署简单

---

## **🎯 能解决什么问题？**

对于：

👉 博客站长

👉 AI 导航站

👉 企业官网

👉 独立开发者

👉 个人主页

都可以轻松了解网站流量情况，不再靠猜测运营。

---

## **☁️ 零成本部署**

无需购买服务器，

直接部署到 Vercel 即可使用。

几分钟就能拥有属于自己的网站统计后台。

真正做到：

💰 零成本

⚡ 速度快

🔒 隐私友好

📊 数据清晰

---

## **📌 最后**

很多人每天都在更新网站，

却从不关注数据。

而 Umami 最大的价值就是：

让你用最简单的方式，看懂网站流量和用户行为。

🔗 项目地址：

```
https://github.com/umami-software/umami
```

这是我在 Vercel 搭建的 umami，效果还不错，数据一目了然。

![Ai星码博客](/img/aixmb/107/01.webp)

![Ai星码博客](/img/aixmb/107/02.webp)

![Ai星码博客](/img/aixmb/107/03.webp)

![Ai星码博客](/img/aixmb/107/04.webp)

**搭建教程：**

**1.免费注册一个vercel账号。**

```
https://vercel.com/
```

**2.打开项目GitHub地址，将代码Fork到自己的账号下。 项目地址**

![Ai星码博客](/img/aixmb/107/05.webp)

**3.注册登陆Vercel进入控制台点击 Projects ，再点击 Add New 。新建项目 点击Projects

![Ai星码博客](/img/aixmb/107/06.webp)**

**4.登陆授权自己的github账号（我已授权过，你们登陆授权），找到该项目点击 Import**

![Ai星码博客](/img/aixmb/107/07.webp)

**5。可以自由填写项目名称，其它全部保持默认即可，此处直接点击Deploy部署即可，由于没有提供环境变量，Vercel 会提示部署失败。不用理会，重新部署关联数据库即可成功。**

**![Ai星码博客](/img/aixmb/107/08.webp)

6.Vercel后台控制面板点击Storage建立数据库

![Ai星码博客](/img/aixmb/107/09.webp)**

**7.创建数据库，类型选择Neon**

![Ai星码博客](/img/aixmb/107/10.webp)

![Ai星码博客](/img/aixmb/107/11.webp)

**8.选地区，我们选择距离近新加坡 下拉底部点击 下一步，数据库名字随填，下拉点击完成。**

![Ai星码博客](/img/aixmb/107/12.webp)

![Ai星码博客](/img/aixmb/107/13.webp)

**9.点击进入刚创建完的数据库进入管理，点击Connect to Project 关联项目最后Connect Project。**

![Ai星码博客](/img/aixmb/107/14.webp)

![Ai星码博客](/img/aixmb/107/15.webp)

**10，返回管理面板点击Deployments，找到部署失败的该项目，点击Redeploy**

**重新部署一次。等待几分钟后就看到部署成功。**

![Ai星码博客](/img/aixmb/107/16.webp)

![Ai星码博客](/img/aixmb/107/17.webp)

**11.返回Projects即可看到该项目在跑了。**

![Ai星码博客](/img/aixmb/107/18.webp)

**12.部署成功后，登录 umami 后台。初始账号密码：****UserName: admin****Password: umami****绑定自定义域名在该项里找到域名修改即可。

![Ai星码博客](/img/aixmb/107/19.webp)**

**13.自定义国内访问域名**

![Ai星码博客](/img/aixmb/107/20.webp)

---

> 本文转载整理自 [Ai星码博客](https://aixmb.com/107.html)，版权归原作者所有。

