#-*- coding: UTF-8 -*-
#!/usr/bin/env python

#导入相关模块
import os
import sys

#定义搭建系统环境的函数
def setup_env():
    #获取python脚本所在目录路径
    dir = sys.path[0]

    os.system("yum install expect curl vim gcc gdb -y")
    os.system("yum remove lvm2 -y")

    #安装docker服务
    os.system("curl -sSL https://get.daocloud.io/docker | sh")
    #os.system("yum install docker -y")

    #安装daocloud监控服务
    os.system("curl -sSL https://get.daocloud.io/daomonit/install.sh | sh -s fc49e03377757c0be73bfb24f52fdecbfaac4f15 ")

    os.system("systemctl start docker")
    os.system("dao pull centos")
    os.system("python2.7 %s/get-pip.py" %dir)
    os.system("pip install xlrd")
    os.system("pip install virtualenv")
    os.system("pip install flask")
    os.system("pip install flask-bootstrap")
    os.system("pip install flask-wtf")

#定义main函数
def main():
    setup_env()

if __name__ == "__main__":
    main()
