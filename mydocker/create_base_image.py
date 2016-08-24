#-*- coding: UTF-8 -*-
#!/usr/bin/env python

#导入相关模块
import os
import sys
import commands

#定义构建基础镜像的函数
def create_base_image():
    #获取python脚本所在目录路径
    dir = sys.path[0]

    #生成公钥密钥
    os.system("rm -rf /etc/ssh/ssh_host_rsa_key*")
    os.system("chmod +x %s/ssh-keygen.exp" %dir)
    os.system("%s/ssh-keygen.exp" %dir)
    os.system("chmod -x %s/ssh-keygen.exp" %dir)
    os.system("cp /etc/ssh/ssh_host_rsa_key* %s" %dir)

    #构建基础镜像
    os.system("docker build -t base:dockerfile %s" %dir)
    os.system("rm -rf %s/ssh_host_rsa_key*" %dir)

    #创建数据卷
    os.system("rm -rf /workspace && mkdir /workspace && chmod 777 /workspace")

    #创建日志数据卷
    os.system("rm -rf /monitor && mkdir /monitor && chmod 777 /monitor")

    print("Base Image successfully constructed!")

#定义main函数
def main():
    (status,output) = commands.getstatusoutput("docker images | grep base")
    if status == 0:
		print("Base Image already exists!")
    else:
        create_base_image()

if __name__ == "__main__":
    main()
