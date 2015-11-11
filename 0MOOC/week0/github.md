# github 私人教程

##常用命令：

- 1、克隆一个目录到本地计算机

`git clone git@github.com:leonpak/gitskills.git`
>其中leonpak为github账号，gitskills.git为gitskills.git中被克隆的目录


- 2、在本地目录修改后

 `git add .`
 >把修改添加到暂存区
 
- 3、查看变化情况
`git status`

- 4、`git commit -m "修改过的备注"`
>注意，要添加修改过的备注，要不然会进入vi模式，然后让你添加备注，如果进入vi模式，`i键` 进入`insert`模式，输入备注，再`esc键`后输入`:wq`保存退出

- 5、最后进行推送到网站`git push`

##问题
- 1、github上修改后与本地克隆的目录不同，产生冲突，不能进行push
>先`git pull`把github上的修改同步到本来目录，再进行push
- 2、要实现本地推送要先将本地ssh-rsa钥匙添加到github的sitting里的SSH key，在终端找到ssh-rsa文件后用cat命令打开

##参考资料
- 1、github常用命令 ![](https://imgur.com/gallery/gFwc5XO/)
- 2、[廖雪峰教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)


