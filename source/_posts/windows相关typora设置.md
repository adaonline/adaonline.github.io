---
title: windows相关typora设置
date: 2024-06-13 02:04:14
tags: hexo
categories:
  - hexo
---



# 如何在windows右键新建中新增“MarkDown File”

### 1.创建一个markDownFile.txt文件，内容如下:

```bat
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\.md]
@="Typora.md"
"Content Type"="text/markdown"
"PerceivedType"="text"
[HKEY_CLASSES_ROOT\.md\ShellNew]
"NullFile"=""
```

### 2.保存文件名，将后缀改为.reg

### 3.双击运行即可

window会有提示确定要继续吗，点确定，然后会提示已经成功添加到注册表中



# 如何设置右键用typora打开文件和文件夹

### 1.找到自己的typora安装位置

我自己的在 D:\Program Files\Typora

### 2.编辑两个文本文件，另存为.reg结尾，内容如下

其中安装位置需要是自己的！

这是两个不同文件

```
Windows Registry Editor Version 5.00
 
[HKEY_CLASSES_ROOT\*\shell\Typora]
"icon"="D:\\Program Files\\Typora\\typora.exe"
@="Open With Typora"
 
[HKEY_CLASSES_ROOT\*\shell\Typora\command]
@="\"D:\\Program Files\\Typora\\typora.exe\" \"%1\""
```

```
Windows Registry Editor Version 5.00
 
[HKEY_CLASSES_ROOT\Folder\shell\Typora]
"icon"="D:\\Program Files\\Typora\\typora.exe"
@="Open With Typora"
 
[HKEY_CLASSES_ROOT\Folder\shell\Typora\command]
@="\"D:\\Program Files\\Typora\\typora.exe\" \"%1"
```

### 3.双击运行即可，有提示点确定

