---
title: hexo日常使用
tags: hexo
---
## Hexo常用

### 安装

需要首先安装nodejs


- window安装
  https://nodejs.org/en
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

### 本地部署

```shell
$ hexo clean #清除缓存
$ hexo g #生成静态文件
$ hexo s #部署运营
```

### 部署到github

```shell
$ hexo deploy
或者
$ hexo d
```

### 创建新文章

```bash
$ hexo new "你的文章标题"
```
