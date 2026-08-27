---
title: 关于-GitHub-的一些事情
date: 2026-08-27 15:07:00
updated: 2026-08-27 15:07:00
tags:
  - 技术
  - github
categories:
  - 技术
---

# 关于 GitHub 的一些事情

> 本篇文章探讨了关于 GitHub 的一些事情。作者提到了 GitHub 上一个项目可以有多种下载到本地的方式，包括在线克隆 fork 到自己仓库、通过链接下载克隆到本地文件夹以及下载 ZIP 解压到本地文件等方法。然后，作者分享了一些遇到的问题和解决方法，例如如何绑定多个 GitHub 账号以及本地怎么部署大文件到 GitHub 上去等。最后，作者总结道：**适合自己才是最好的**，还有许多未知未解之谜等待我们去发掘。
>
> ⚠️ *It has been 853 days since the last update, the content of the article may be outdated.*

---

## 前言

事情是这样的，最近因为在研究几个项目，准备搭建各种关于个人的主页和模板，开始踏入我的代码研究以及 GitHub 部署等征途。大概今天的任务就是为了 fork 大佬的一个模板，但是因为发现有很多代码需要修改，加之在线修改很难去操作等，所以直接从 GitHub 上下载出来，但是在后面遇到了一系列的困难，所以发现还是有很多要学的东西！

---

## GitHub 项目下载方式

从目前对 GitHub 的了解，一个项目可以有多种下载到本地的方式：

### 方式一：在线克隆 Fork 到自己仓库

这种方式——直接在线 fork 一下，对于开源的仓库，我们都是可以看得到，所以直接到原作者或者二改开源作者那里一键 fork 到自己的仓库就可以。但是此种方法有很多限制，例如：有 fork 标记，且各种别人的仓库信息挂在自己的仓库上，显得非常不美观，且感觉就是偷来的东西，而且还被别人打上了标签。因此，实在是无法操作可能，**不推荐此种方法！**

- **优点**：方便快捷，克隆速度快，不用再次部署到 GitHub，相当于直接备份！
- **缺点**：复制克隆生搬硬套，不好修改，容易出现问题，不方便了解项目的具体内容。

### 方式二：通过链接下载克隆到本地文件夹

首先，找到想要的项目开源代码主页，找到 `Code` 选项下的 HTTP 或者 SSH，选择第一排或者第二排等，直接点击 `git clone` 然后复制，再到本地创建一个新的文件夹，直接打开 **Git Bash Here**，然后把刚才的项目地址直接粘贴运行，跑程序式克隆项目到本地即可。

- **优点**：较方便快捷，可修改程度高，了解代码项目的具体内容更加方便快捷！
- **缺点**：部署到其他 Git 平台不方便，且容易丢失文件，且项目的部署方式麻烦，每次修改都得部署一次！

### 方式三：下载 ZIP 解压到本地文件

还是找到想要的项目开源代码主页，到 `Code` 栏中，下面几列，直接打包下载 ZIP 文件，然后解压到本地文件夹里。注意一下，这种方式下载还是限制会比较大，因为网速和国内访问速度差异，有时候下载会非常慢，甚至卡断。因此这种方式下载，最好选择一些镜像服务下载 ZIP。而这种方式是相比于第一种更加直接，相对于第二种，很多项目会提供下载镜像，下载方便。

- **优点**：下载方便，一键下载，本地解压，速度也较快。
- **缺点**：没有镜像服务，基本下载几 KB/s，而且容易下载出问题。

---

## 新手实操问题

再接下来，就是我遇到的一些问题了，一些关于 GitHub 相对于"小白"新手，真正难的实操问题：

**Q1**：一台电脑怎么绑定多个 GitHub 账号？怎么好像只能生成一个 SSH Key？

**W1**：由于前面发现，一个 GitHub 账号只能提供一个静态的域名 Page 服务，所以还想要再白嫖一个永久的域名 Page，然后把以后的工作转移到这个网站上。——（此方法已经由 ChatGPT 解决，几乎解决 80% 问题！）

**Q2**：本地多个大文件（<100M）怎么部署到 GitHub 上去？

**W2**：因为 fork 了一位大佬的模板主题，准备修改好，然后看看效果，但是一直找不到方法，部署到 GitHub 仓库里去。之前的是 Hexo 主题，直接在配置文件里配置一下就行。但是这个不一样，所以得去学习一下。因此才写下这篇文章，记录保留一些方法！

---

## 一台电脑绑定多个 GitHub 账号

> 方法：（来源于 ChatGPT —— AIchatOS）

在一台电脑上绑定多个 GitHub 账号的 SSH 密钥，可以按照以下步骤操作：

### 1. 生成新的 SSH 密钥对

打开终端，输入以下命令生成一个新的密钥：

```bash
ssh-keygen -t rsa -C "your-email@example.com" -f ~/.ssh/github2_rsa
```

### 2. 添加新的 SSH 密钥到 SSH 代理

输入以下命令将新密钥添加到 SSH 代理：

```bash
ssh-add ~/.ssh/github2_rsa
```

### 3. 将新的 SSH 公钥添加到 GitHub

将新生成的公钥（`~/.ssh/github2_rsa.pub`）的内容添加到 GitHub 账号的 SSH keys 页面。在 GitHub 页面上选择 **Settings** > **SSH and GPG keys** > **New SSH key**，在 **Key** 框中粘贴公钥内容并保存。

### 4. 设置 Git 全局用户名和邮箱

在终端中输入以下两行命令分别设置 Git 全局用户名和邮箱：

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

### 5. 配置 SSH config 文件

打开并编辑 SSH config 文件（通常位于 `~/.ssh/config`），在文件中添加以下内容：

```bash
# Default GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa

# Second GitHub (use a different SSH key)
Host github.com-second-account
    HostName github.com
    User git
    IdentityFile ~/.ssh/github2_rsa
```

### 6. 测试 SSH 连接

输入以下命令测试 SSH 连接：

```bash
ssh -T git@github.com
ssh -T git@github.com-second-account
```

如果两次都能成功连接，就说明绑定多个 GitHub 账号的 SSH 密钥已经完成。

> 🍬🍬 漂亮！
>
> 通过上面的方法，成功解决，原来只要在电脑上多生成几个 SSH Key，绑定一下邮箱和用户名即可！此方法可以白嫖多个账号，多个 Page 域名。但是比较这种方法，需要注册账号，创建仓库等。且，如果仓库账号不用，或者用不着，会导致冷藏库情况，并且多账户难管理和重新部署，容易成为死仓！

### 补充说明

对了，在生成了仓库之后，又发现了各种情况，例如两个账号部署容易冲突，虽然可以绑定 Git 地址，但是……但是……发现无法直接通过这种方式去 fork 自己的仓库到另外一个账号的仓库上，而直接生成出 Page 访问域名。

因为好像原因是不能直接 `.github.io` 生成 Page 文件，需要自行创建。虽然 fork 可以直接命名仓库，但是我也想这样投机取巧，后来发现了，它还是不能直接生成 Page 静态的域名访问地址，后台 Setting 也无法设置。且打开来的还是 404 页面！！

而后就只能自己创建一个原始仓库，然后想办法把项目一五一十的部署上来了！！最终成功又部署了一条 GitHub 线路备用！——也许其中有猫腻，但是还是老老实实写项目，上传比较稳妥些！

---

## 本地文件怎么部署到 GitHub 上？

自己总结出来：

### 方法一：直接上传文件

Add files 然后把文件上传上去，但是这种只有 10 个小文件，不能很好的分类上传完成！！

### 方法二：GitHub Desktop 桌面客户端

百度了一下，度娘上说，可以下载 GitHub Desktop 桌面客户端版，然后用客户端上传大部分文件！

### 方法三（推荐）：Git 命令行部署

用 CSDN 上的方法，直接 Git 部署，比较方便。但是这种比较稳定，不能后期更新，需要重新部署应该！

> ——— 这是目前我已知的方法！！

### 详细方法：通过 Git 命令上传

#### 第一种方法（针对自带 Git 配置的项目）

通过把远程仓库文件克隆下来，再添加自己需要上传的文件，再上传到远程仓库。

#### 第二种方法（针对没有自带 Git 配置的项目）

**第一步**：我们需要先创建一个文件夹（其实也就是一个文件夹，我的这个文件夹叫 `repository`）。

你可以直接桌面右击新建文件夹，也可以右击打开 Git Bash 命令行窗口通过命令来创建。

**第二步**：在 `repository` 文件夹里创建一个 `test110` 的文件夹（仓库），通过命令 `git init` 把这个文件夹变成 Git 系统可管理的仓库（进入 `test110` 文件夹打开 Git Bash）。

**配置 Git 系统的用户基本信息**（推荐选全局配置）

作用：
1. 用户名和邮箱地址是本地 Git 客户端的一个变量
2. 每次 commit 都会用用户名和邮箱记录
3. GitHub 的 contributions 统计就是按邮箱来统计的

**配置全局用户名和邮箱**（适用于所有仓库）：

```bash
# 配置全局用户名
git config --global user.name "用户名"

# 配置全局邮箱
git config --global user.email "邮箱"
```

**配置单一仓库用户名和邮箱**（指定的仓库）：

```bash
git config user.name "用户名"
git config user.email "邮箱"
```

**查看配置信息命令**：

```bash
git config --list
```

---

### 方法三的原理和步骤

以我理解：

先创建个仓库，且包含一个文件 `README.md`，然后通过克隆这个仓库到本地，与本地产生联系，再把自己想要上传的文件主体部分，直接通过 Git Bash 命令，上传到这个仓库。

**注意几点**：

由于只是产生了一定的联系，但是还是要重新绑定账号等，并且需要注意文件里，不能把别人项目里的 `.git` 复制过来，只要一些主体文件就行。（有时间，还是建议自己从底层搭建，若因为只是一时兴趣，所以还是研究一下部署文件比较好！！）

---

### 详细步骤：本地部署到 GitHub

> 🎁🔨 CSDN 本地部署到 GitHub 上（详细版，因为我已经知道了，所以去除图片，需要详细了解，可直接跳转到原文查看：[如何上传文件到 GitHub（图文）](https://blog.csdn.net)）

接下来进入正题，如何上传文件到 GitHub。

#### 1. 注册一个 GitHub 账号

因为我之前用下载程序之类的注册挺久了，所以具体怎么操作不太记得了。要是国内的网址不太好使，试试国外的会很 nice。

#### 2. 下载一个 Git Bash 版本控制软件

下载地址官网：[Git - Downloads](https://git-scm.com)

这个软件安装没什么好注意的，一路 next 就行，想改路径就在能改的地方改就行。

#### 3. 启动 Git Bash

一个简单的方法，直接进入要上传的文件路径下，空白处点击右键，点击 **Git Bash Here**。

#### 4. 连接 Git Bash 与 GitHub

这一步只需要在第一次使用时操作就好。

打开 Git Bash 后输入如下代码：

```bash
git config --global user.name "your name"
git config --global user.email "your_email@youremail.com"
```

之后会弹出网页，按照要求输入账号密码就好。

#### 5. 在 GitHub 上创建 Repository

点击右侧头像下 **Your Repositories**。

#### 6. 上传文件

```bash
git init                          # 初始化仓库
git add README.md                 # 可以替换为 git add . 意为上传文件夹下的所有文件
git commit -m "first commit"      # 提交备注
git branch -M main                # 重命名分支为 main
git remote add origin https://github.com/lixiaoling2468/test.git  # 这里地址会变
git push -u origin main           # 上传文件
```

顺利在这一步后就成功了，再去 GitHub 上查看，可以发现文件上传了。

---

### 上传部署时一些重要的 Git 命令汇总

**cd 进入克隆的这个文件夹**：

```bash
cd + 文件夹名字
```

**依次输入以下代码**：

```bash
git init
git add .
git commit -m "你的提交信息"
```

**注意**：会要求输入

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

来确定你的身份和上传的账号。

**main 分支部署**：

```bash
git branch -M main

git remote add origin https://github.com/xxxxx/xxxx.git  # 这里地址会变

git push -u origin main  # 上传文件
git push
```

依次输入以上代码后，进入 GitHub 查看：文件夹已上传 GitHub，上传成功。

---

## 最后

总结一下：

不管前面那种仓库下载项目也好，还是怎么部署项目或者上传文件也好，需要根据个人情况看，尤其是项目的特点，还有个人喜好等。因此**适合自己才是最好的**，还有 GitHub 上，还有许多未知未解之谜，待我们一起去慢慢发掘！！
```