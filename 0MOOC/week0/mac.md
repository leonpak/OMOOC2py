# 基础准备 
背景：Mac osx 


## Mac 终端基本命令

- 目录操作

命令名                       功能描述                                             使用举例

`mkdir `                        创建一个目录                                       `mkdir dirname`

`rmdir`                         删除一个目录                                       `rmdir dirname`

`mvdir     `                   移动或重命名一个目录                         `mvdir dir1 dir2`

`cd      `                       改变当前目录                                       `cd dirname`

`pwd    `                      显示当前目录的路径名                          `pwd`

`ls        `                      显示当前目录的内容                             `ls -la`

 

- 文件操作

命令名                                 功能描述                                  使用举例

`cat        `                              显示或连接文件                       `cat filename`

 

 

`od             `                          显示非文本文件的内容            `od -c filename`

`cp             `                         复制文件或目录                        `cp file1 file2`

`rm       `                              删除文件或目录                         `rm filename`

`mv        `                            改变文件名或所在目录               `mv file1 file2`

 

`find        `                          使用匹配表达式查找文件            ` find . -name "*.c" -print`

`file       `                           显示文件类型                                `file filename`

- 选择操作

命令名                             功能描述                                       使用举例

`head          `                    显示文件的最初几行                       `head -20 filename`

`tail          `                       显示文件的最后几行                       `tail -15 filename`

`cut       `                         显示文件每行中的某些域                 `cut -f1,7 -d: /etc/passwd`

`colrm      `                      从标准输入中删除若干列                  `colrm 8 20 file2`

 

`diff      `                          比较并显示两个文件的差异            `    diff file1 file2`

 

 

`sort         `                    排序或归并文件                                      `sort -d -f -u file1`

`uniq             `              去掉文件中的重复行                                  `uniq file1 file2`

`comm       `                 显示两有序文件的公共和非公共行              `comm file1 file2`

`wc    `                        统计文件的字符数、词数和行数                    `wc filename`

`nl      `                       给文件加上行号                                         `nl file1 >file2`

 

 

 

 

- 进程操作

命令名                     功能描述                                                 使用举例

`ps        `                   显示进程当前状态                                     `ps u`

`kill     `                    终止进程                                                     `kill -9 30142`

 

 

- 时间操作

命令名                           功能描述                                            使用举例

`date    `                显示系统的当前日期和时间                           `date`

`cal        `                           显示日历                                       `cal 8 1996`

`time   `                      统计程序的执行时间                            `time a.out`

- 网络与通信操作

命令名                                功能描述                                       使用举例

`telnet    `                              远程登录                                 `telnet hpc.sp.net.edu.cn`

`rlogin  `                               远程登录                                 `rlogin hostname -l username`

`rsh       `                在远程主机执行指定命令                             `rsh f01n03 date`

`ftp   `                在本地主机与远程主机之间传输文件                `ftpftp.sp.net.edu.cn`

`rcp     `            在本地主机与远程主机 之间复制文件               `rcp file1 host1:file2`

`ping    `               给一个网络主机发送 回应请求                   `ping hpc.sp.net.edu.cn`

`mail    `                      阅读和发送电子邮件                                          `mail`

`write    `                  给另一用户发送报文                                  `write username pts/1`

`mesg      `              允许或拒绝接收报文                                                 `mesg n`


