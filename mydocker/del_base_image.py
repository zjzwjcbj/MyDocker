#-*- coding: UTF-8 -*-
#!/usr/bin/env python

#导入相关模块
import os
import sys
import commands

#定义删除基础镜像的函数
def del_base_image():
    #获取python脚本所在目录路径
    dir = sys.path[0]

    #删除基础镜像
    os.system("docker rmi base:dockerfile")

    #删除数据卷
    os.system("rm -rf /workspace")

    #删除日志数据卷
    os.system("rm -rf /monitor")

    print("Base Image successfully deleted!")

#定义main函数
def main():
    (status,output) = commands.getstatusoutput("docker images | grep base")
    if status == 0:
        del_base_image()
    else:
		print("Base Image does not exist or has been deleted!")

if __name__ == "__main__":
    main()
