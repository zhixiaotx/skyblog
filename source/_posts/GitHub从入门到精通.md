---
title: GitHub从入门到精通
date: 2026-08-27 15:07:00
updated: 2026-08-27 15:07:00
tags:
  - 技术
  - github
categories:
  - 技术
---

# 万字长文｜GitHub 从入门到精通

> **作者**：Miles  
> **来源**：Miles的AI日记（微信公众号）  
> **原文链接**：[https://mp.weixin.qq.com/s/1FickGzrNjIc5UE-pOU_IA](https://mp.weixin.qq.com/s/1FickGzrNjIc5UE-pOU_IA)

---

如果你想用 GitHub 赚钱，最直接的路并不复杂：在许可证允许的前提下，找到有价值的开源项目，把部署、中文说明和售后做成服务，再去各类平台卖交付。

但是真正能收钱的是信息筛选和落地能力。想做 AI、转 FDE，或者把自己变成一家 OPC，代码、文档、版本和协作早晚都会落到 GitHub 上。

哪怕你做的是创作和自媒体，GitHub 上也有大量选题工具、自动化项目和内容生产流程，可文件一多、AI 一改，没有 Git 管版本，很快就会失控。所以，程序员要学，做项目、做内容的人也一样；它决定你能不能把灵感变成一个可管理、可复用、能交付的项目。

这篇我断断续续磨了大半个月，从 0 到 1 把 Git、GitHub、Commit、分支、PR 和常见报错都实操了一遍，之后的直播也会沿着同一套流程来讲。正式开播前，我先把这份教程开源出来，大家可以先收藏，也可以跟着完整做一遍。

---

## 一、Git 和 GitHub，到底谁管什么

Git 是装在电脑里的版本管理工具。断网时，你仍然可以提交、看历史、建分支和合并。GitHub 是远程仓库与协作平台，它接收 Git 推上来的提交，再提供 Issues、Pull Requests、Actions、代码审查和权限管理。

Git 最容易混的，是同一份修改会处在四个不同位置。下面这张信息图把工作区、暂存区、本地仓库和远程仓库拆成了四层。

- **工作区**：你正在编辑的文件
- **暂存区**：`git add` 后文件暂存的位置
- **本地仓库**：`git commit` 后保存的版本历史
- **远程仓库**：`git push` 后推送到 GitHub 的代码

按下保存，只会把内容写进硬盘。`git add` 负责挑选，`git commit` 在本地留下版本，`git push` 才把这些提交送到 GitHub。

所以提交前要看 diff、实际运行或测试；推送成功后，再去网页回查。这样出了问题，你能马上知道它停在哪一层。

---

## 二、动手前，只准备四样东西

你需要 Git、一个 GitHub 账号、一个编辑器和一个练习项目。编辑器用 VS Code 就够了，项目可以是一张网页，也可以是一份 Markdown 文档。

先在终端确认 Git：

```bash
git --version
```

这次演练使用的是 macOS 和 Git 2.49.0。Windows 用户可以用 Git Bash 或 VS Code 内置终端，下面的 Git 命令相同。

接着配置提交作者：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

这是写进提交记录的作者信息，不负责登录 GitHub。如果你只想给当前练习项目配置，把 `--global` 换成 `--local`。

GitHub 的登录是另一件事。命令行常用三种方式：

- **GitHub CLI**，通过 `gh auth login` 打开浏览器授权；
- **HTTPS**，使用 Personal Access Token 或凭据管理器；
- **SSH**，把公钥添加到 GitHub，后续通过密钥认证。

刚入门可以选 GitHub CLI 或 HTTPS。使用 HTTPS 时，终端要求 Password 就填写 Token，普通账号密码已经不适用。**Token 不要写进命令、远程 URL、README、聊天和截图。**

---

## 三、别急着 init，先确认终端到底在哪

这次练习从一个普通网页开始。它能在浏览器打开，但还没有任何 Git 历史。

项目里有三个文件：

```
index.html
style.css
.gitignore
```

在 VS Code 选择「打开文件夹」，不要只点开一个 HTML 文件。然后在内置终端运行：

```bash
pwd
ls
```

`pwd` 显示当前目录，`ls` 列出文件。看到 `index.html` 和 `style.css` 以后再继续。

这个检查看着很笨，却能挡住最麻烦的一类事故：有人在桌面、Documents，甚至用户主目录执行 `git init`，随后 `git add .` 把几千个无关文件放进暂存区。Git 没坏，目录选错了。

---

## 四、git init 做了什么

现在初始化仓库：

```bash
git init -b main
git status --short
```

`git init -b main` 在当前目录创建 `.git`，并把初始分支命名为 `main`。`.git` 是一个隐藏目录，提交、分支、暂存区、远程地址等信息都放在里面。项目文件还在原处，Git 从这一刻开始观察它们。

截图里的 `??` 表示未跟踪。文件已经存在，Git 还没决定要不要记录。

想确认仓库根目录，可以运行：

```bash
git rev-parse --show-toplevel
```

输出应该是当前项目文件夹。若提示 `fatal: not a git repository`，先检查目录，再看是否执行过 `git init`。

---

## 五、第一次提交，先留住一个可靠起点

项目还没修改，为什么要先提交？因为后面所有变化都需要一个可比较的起点。先在浏览器打开网页，确认标题、卡片和报名区能显示；把窗口缩窄，看看手机宽度有没有横向滚动。

再看 `.gitignore`。这次使用的内容是：

```
.env
.env.*
*.log
node_modules/
dist/
build/
```

`.gitignore` 用来挡住密钥、日志、依赖和构建产物。它主要对尚未跟踪的文件生效。一个密钥如果已经提交过，后来补上 `.gitignore`，那段历史还在，真正的处理还包括吊销或轮换密钥。

开始挑选第一次提交的文件：

```bash
git add index.html style.css .gitignore
git status --short
git diff --cached --stat
```

状态中的 `A` 是 Added，表示文件已经进入暂存区。`git diff --cached --stat` 会告诉你这次准备提交几个文件、大概改了多少行。想看具体内容，运行：

```bash
git diff --cached
```

确认以后提交：

```bash
git commit -m "chore: 初始化校园 AI 招新页"
git log --oneline
git status
```

Commit 可以理解成带作者、时间、说明和父提交的项目快照。`ffdf4ff` 是这次提交哈希的短写，在当前仓库中用它就能准确定位版本。

`feat`、`fix`、`docs`、`style`、`chore` 是常见的提交类型，并非 Git 强制语法。比前缀更重要的是后面的中文：做了什么，改了哪个对象，为什么做。

---

## 六、第二次提交：把 AI 的修改当成待审稿

接下来给页面加一个「查看报名方式」按钮。使用 AI 编程工具时，我会把边界写进提示词：

```
只修改 index.html，在介绍文字下方增加"查看报名方式"链接，
链接到页面内的 #apply。不要修改 style.css，不要执行 Git 提交。
完成后告诉我改了哪个文件。
```

手工修改也很简单：

```html
<a class="cta" href="#apply">查看报名方式</a>
```

AI 说完成了，先别提交。运行：

```bash
git status --short
git diff -- index.html
git diff --check
```

`git diff` 显示工作区里尚未暂存的变化。绿色 `+` 是新增行，红色 `-` 是删除行。`git diff --check` 没有输出，说明没有发现明显的尾随空格等格式问题；它不会替你检查按钮能不能点。

回到浏览器刷新，点击按钮，再把窗口缩窄。页面应该滚动到报名区，按钮和卡片在窄屏下仍然正常。

测试通过后才提交：

```bash
git add index.html
git diff --cached
git commit -m "feat: 新增报名入口，方便快速查看申请方式"
git log --oneline -2
```

这时仓库里有两个能说清楚的版本：起始页和报名按钮。以后按钮出问题，可以直接找到它是哪次加进来的。

顺便把两个 diff 分清：

```bash
git diff              # 工作区与暂存区之间的差异
git diff --cached     # 暂存区与最近一次提交之间的差异
```

如果 `git diff` 没输出，文件可能没保存，也可能已经暂存或提交。依次看 `git status`、`git diff --cached` 和 `git log`，比反复输入 `git add .` 靠谱。

---

## 七、分支：给不确定的改动留一个试验位置

按钮只增加一行，风险不大。把整套主题从紫色改成橙色，结果可能好看，也可能很俗，这种修改适合放进分支。

```bash
git switch -c experiment/warm-theme
git branch --show-current
```

分支在概念上是指向某个提交的名字。新分支刚创建时与 `main` 指向同一提交，所以文件完全一样。等实验分支产生新提交，两条线才分开。

图里蓝色的 `main` 仍指着第二次提交，橙色的 `experiment` 已经指向第三次提交。项目并没有复制出两套文件，变化的只是两个分支名分别指向哪里。

修改 `style.css` 的颜色变量，刷新页面确认以后提交：

```bash
git diff -- style.css
git diff --check
git add style.css
git commit -m "style: 在实验分支试用暖色主题"
git log --oneline --graph --decorate --all
```

`HEAD` 表示你当前站在哪里。截图里 `HEAD` 指向 `experiment/warm-theme`，`main` 仍停在按钮提交。

确定保留暖色主题，切回 `main` 合并：

```bash
git switch main
git merge experiment/warm-theme
```

`main` 没有产生分叉，Git 直接把 `main` 指针向前移动到实验提交。

---

