---
title: 初入hexo
date: 2023-05-23 00:42:57
tags: hexo
categories:
  - hexo
---
## Hexo安装步骤

### 安装

需要首先安装nodejs

- window安装
  https://nodejs.org/en
  
  推荐使用nvm管理nodejs:[**[nvm-windows](https://github.com/coreybutler/nvm-windows)**](https://github.com/coreybutler/nvm-windows)
  
- linux安装

  ```shell
  <!-- 操作系统版本 -->
  $ cat /proc/version
  Linux version 5.10.0-19-amd64 (debian-kernel@lists.debian.org) (gcc-10 (Debian 10.2.1-6) 10.2.1 20210110, GNU ld (GNU Binutils for Debian) 2.35.2) #1 SMP Debian 5.10.149-2 (2022-10-21)
  <!-- 发型版本 -->
  $ cat /etc/os-release
  PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
  NAME="Debian GNU/Linux"
  VERSION_ID="11"
  VERSION="11 (bullseye)"
  VERSION_CODENAME=bullseye
  ID=debian
  HOME_URL="https://www.debian.org/"
  SUPPORT_URL="https://www.debian.org/support"
  BUG_REPORT_URL="https://bugs.debian.org/"
  ```

  安装

  ```shell
  sudo apt-get update
  sudo apt-get install nodejs
  sudo apt-get install npm
  查看版本
  nodejs --version(这时候可能版本较低)
  升级版本，模块n管理版本
  sudo npm install -g n
  升级到稳定版
  sudo n stable
  ```

### 安装hexo

```shell
$ npm install -g hexo-cli
```

### 初始化一个hexo项目

```bash
$ hexo init <folder>
$ cd <folder>
$ npm install
```

创建完成后的目录为

```text
.
├── .github
├── node_modules
├── scaffolds
├── source
	└── _posts
		└── hello-world.md
├── themes
├── .gitignore
├── package-lock.json
├── package.json
└── _config.landscape.yml
```

### 开始写作

```bash
$ hexo new [layout] "你的文章标题"
```

layout是布局，可以暂时忽略，如果指定了布局，hexo会到scaffolds文件夹下找，这些布局会被一些主体用到

```bash
$ hexo new "My Gallery"
```

会创建一个My Gallery标题的文章储存到 `source/_posts` 文件夹

编辑_posts文件夹下的md文件，然后部署就可以看到效果了

### 本地部署

```bash
$ hexo clean #清除缓存
$ hexo g #生成静态文件
$ hexo s #部署运营
```

### 部署到github

```yml
#需要在_config.yml中提前设置好自己的deploy内容
deploy:
  type: git
  repo: https://github.com/adaonline/adaonline.github.io.git
  branch: master
```

部署命令

```bash
$ hexo deploy
或者
$ hexo d
```

### 从github拉取

在.gitignore指定了不上传node_modules

如果是异地拉取这个仓库，需要初始化hexo环境，要不然会提示hexo各种报错

需要nodejs环境，并且安装了hexo，在库目录下执行npm install即可

### 测试图片

![1](../images/hexo日常使用/saierda.jpg)
