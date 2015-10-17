# 基础准备 
背景：Mac osx 


## Mac 终端基本命令

- 目录操作

命令名                       功能描述                                             使用举例

mkdir                        创建一个目录                                       mkdir dirname

rmdir                         删除一个目录                                       rmdir dirname

mvdir                        移动或重命名一个目录                         mvdir dir1 dir2

cd                             改变当前目录                                       cd dirname

pwd                          显示当前目录的路径名                          pwd

ls                              显示当前目录的内容                             ls -la

 

- 文件操作

命令名                                 功能描述                                  使用举例

cat                                      显示或连接文件                       cat filename

 

 

od                                       显示非文本文件的内容            od -c filename

cp                                      复制文件或目录                        cp file1 file2

rm                                     删除文件或目录                         rm filename

mv                                    改变文件名或所在目录               mv file1 file2

 

find                                  使用匹配表达式查找文件             find . -name "*.c" -print

file                                  显示文件类型                                file filename

- 选择操作

命令名                             功能描述                                       使用举例

head                              显示文件的最初几行                       head -20 filename

tail                                 显示文件的最后几行                       tail -15 filename

cut                                显示文件每行中的某些域                 cut -f1,7 -d: /etc/passwd

colrm                            从标准输入中删除若干列                  colrm 8 20 file2

 

diff                                比较并显示两个文件的差异                diff file1 file2

 

 

sort                             排序或归并文件                                      sort -d -f -u file1

uniq                           去掉文件中的重复行                                  uniq file1 file2

comm                        显示两有序文件的公共和非公共行              comm file1 file2

wc                            统计文件的字符数、词数和行数                    wc filename

nl                             给文件加上行号                                         nl file1 >file2

 

 

 

 

- 进程操作

命令名                     功能描述                                                 使用举例

ps                           显示进程当前状态                                     ps u

kill                         终止进程                                                     kill -9 30142

 

 

- 时间操作

命令名                           功能描述                                            使用举例

date                    显示系统的当前日期和时间                           date

cal                                   显示日历                                       cal 8 1996

time                         统计程序的执行时间                            time a.out

- 网络与通信操作

命令名                                功能描述                                       使用举例

telnet                                  远程登录                                 telnet hpc.sp.net.edu.cn

rlogin                                 远程登录                                 rlogin hostname -l username

rsh                       在远程主机执行指定命令                             rsh f01n03 date

ftp                   在本地主机与远程主机之间传输文件                ftpftp.sp.net.edu.cn

rcp                 在本地主机与远程主机 之间复制文件               rcp file1 host1:file2

ping                   给一个网络主机发送 回应请求                   ping hpc.sp.net.edu.cn

mail                          阅读和发送电子邮件                                          mail

write                      给另一用户发送报文                                  write username pts/1

mesg                    允许或拒绝接收报文                                                 mesg n



## Markdown基本语法
1.标题设置（让字体变大，和word的标题意思一样）

在Markdown当中设置标题，有两种方式：
第一种：通过在文字下方添加“=”和“-”，他们分别表示一级标题和二级标题。
第二种：在文字开头加上 “#”，通过“#”数量表示几级标题。（一共只有1~6级标题，1级标题字体最大）

2.块注释（blockquote）

通过在文字开头添加“>”表示块注释。（当>和文字之间添加五个blank时，块注释的文字会有变化。）

3.斜体

将需要设置为斜体的文字两端使用1个“*”或者“_”夹起来

4.粗体

将需要设置为斜体的文字两端使用2个“*”或者“_”夹起来

5.无序列表

在文字开头添加(*, +, and -)实现无序列表。但是要注意在(*, +, and -)和文字之间需要添加空格。（建议：一个文档中只是用一种无序列表的表示方式）

6.有序列表

使用数字后面跟上句号。（还要有空格）

7.下划线

在空白行下方添加三条“-”横线。（前面讲过在文字下方添加“-”，实现的2级标题）