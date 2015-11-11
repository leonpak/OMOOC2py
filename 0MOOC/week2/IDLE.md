# 解决IDLE中文输入问题

## 背景
Mac osx 10.11
python 2.7.10

##问题
中文输入失效

##分析1
IDLE 界面使用的 Tkinter 需要依赖 Tcl/Tk，而系统自带的 Tcl/Tk 版本太低，造成了不兼容的问题。

##方法1
更新TCL/Tk

##结果
问题依旧存在

##分析
终端下使用命令

`where python`
发现只有一个python

`where wish`
发现有两个wish

```
/usr/bin/wish
/usr/local/bin/wish
```
发现程序依赖的TCL/Tk在
`
/../../../Library/Frameworks/Tk.framework/Versions/8.5
`
而发现更新的版本装在
`
/../../System/Library/Frameworks/Tk.framework/Versions/8.5
`
##方法2

所以把更新的版本复制后直接黏贴覆盖程序依赖所在版本目录

##问题2
发现root账号也修改不了bin目录

##分析
OSX 10.11 版本，引入了新的 Rootless，也就是说：

```
即使是root用户，将无法对以下路径有写和执行权限：
/System
/bin
/sbin
/usr (except /usr/local)
只有Apple自身签名的软件（含命令行工具）可以。
```

##方法3
关闭Rootless权限的方法

```
1、开机按住Command + R键，让电脑进入恢复模式
2、打开终端，在终端中键入：csrutil disable 并回车
3、重新启动电脑进入普通模式即可。
```

##结果
重新执行方法2，中文输入问题解决

