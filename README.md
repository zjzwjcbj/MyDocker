# 基于Docker的在线实验管理系统 #

# 系统功能介绍 #

***

对于程序设计类课程，传统的上机实验方式是学生在各自的实验机器上编写、修改、运行程序，这种方式难以实现对实验环境和程序的集中化管理，难以对学生的实验行为进行监控，也不便于老师对实验中存在的问题进行分析。本系统可以在服务器（目前仅支持单台）上使用docker为每个学生建立实验环境的容器，学生使用默认用户登录，方可进行编写程序，编译、运行程序。同时，系统将会监控学生的登录记录和实验行为，并能够对学生的程序进行备份，除此之外，还可以对学生程序进行重复率检测，防止同学相互抄袭程序。

# 程序目录结构及介绍 #

***

> mydocker

|文件|说明|
|:--:|:--:|
|batch_create_client.py|批量创建客户端容器|
|batch_create_server.py|批量创建服务端容器|
|batch_delete_client.py|批量删除客户端容器|
|batch_delete_server.py|批量删除服务端容器|
|collect_cfile.sh|查找系统中的C语言程序并复制到/home/admin/workspace中|
|compareclientc.py|对客户端C语言程序进行重复率检测|
|compareserverc.py|对服务端C语言程序进行重复率检测|
|create_base_image.py|基于CentOS官方Docker镜像创建实验环境基础镜像|
|del_base_image.py|删除基础镜像|
|Dockerfile|用于创建基础镜像的Dockerfile文件|
|get-pip.py|安装pip脚本|
|history.py|读取历史命令记录文件并显示（对时间格式进行转换）|
|lastlog.sh|记录用户登录记录|
|mydocker|提供的系统CLI|
|profile|添加到/etc/profile中的配置|
|run.sh|Dockerfile中使用的SSH启动脚本|
|setup_env.py|自动安装本系统的脚本|
|showip.sh|Dockerfile中使用的用于在用户登录时显示本机IP的脚本|
|ssh-keygen.exp|自动生成SSH密钥脚本|
|unpe|网络编程环境需要添加的头文件存放目录|
|virc_vimrc|Dockerfile中使用的Vim和Vi的配置文件|

> myweb

|文件|说明|
|:--:|:--:|
|access.log|访问日志|
|run.py|web服务启动脚本|
|startup.sh|自动安装web服务脚本|
|static|静态资源目录|
|templates|模板文件目录|
|uploads|上传文件存放目录|

# 系统安装部署步骤 #

***

操作系统：CentOS7.1（CentOS-7-x86_64-Minimal-1503-01）

    # git clone https://github.com/xautlmx/MyDocker.git
    # cp -r MyDocker/mydocker/* /usr/local/sbin/
    # mydocker --initenv
    # mydocker --createbaseimage
    # cd MyDocker/myweb/
    # bash startup.sh
    
至此安装完成，可以通过mydocker命令管理本系统也可以访问http://IP:5000管理本系统

# mydocker命令帮助说明 #

***

```
Usage: mydocker [OPTION]... [PARAMETER]...
Manage online test management system

Available parameters are as follows:
  --initenv		Installation and Configuration docker and related python module
  --createbaseimage	Automatic build the students' experimental environment based image by dockerfile
  --delbaseimage	Remove the students' experimental environment based image
  --bcreatesrv		Batch create The Server Container
  --bcreatecli		Batch create The Client Container
  --bdelsrv		Batch delete The Server Container
  --bdelcli		Batch delete The Client Container
  --startsrv		Start The Server Container by Student ID
  --startcli		Start The Client Container by Student ID
  --stopsrv		Stop The Server Container by Student ID
  --stopcli		Stop The Client Container by Student ID
  --restartsrv		Restart The Server Container by Student ID
  --restartcli		Restart The Server Container by Student ID
  --statussrv		Check the status of The Server Container by Student ID
  --statuscli		Check the status of The Client Container by Student ID
  --srvlastlog		Check The User Login Information of The Server Container by Student ID
  --clilastlog		Check The User Login Information of The Client Container by Student ID
  --history		Check The Container's History Command Record
  --checkserverc	Detection The Server Code Repetition Rate
  --checkclientc	Detection The Server Code Repetition Rate
  --help		Display this Help and Exit

AUTHOR
  Written by Koenli.
```