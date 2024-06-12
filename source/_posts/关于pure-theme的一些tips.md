---
title: 关于pure theme的一些tips
date: 2024-06-13 01:49:47
tags: hexo
categories:
  - hexo
---

在一些左侧侧边栏，刚搭建完是有首页、归档.....关于等一些内容
但是大部分是需要自己定制的
可以将themes\pure\_source 目录下的内容复制到自己的source目录下
执行
```
hexo clean
hexo g
hexo s
```
在本地查看，即可发现对应的页面已经不再是404
相关的一些内容配置，是在主题配置的_config.yml中