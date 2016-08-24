#-*- coding: UTF-8 -*-
#!/usr/bin/env python

#导入相关模块
import os
import sys
import time

#定义读取用户历史命令的函数
def read_history(*argv_list):
    #获取python脚本所在目录路径
    dir = sys.path[0]

    #判断传入参数数目是否符合要求
    if len(argv_list[0]) != 4:
        print("Usage: %s/mydocker --history {Server/Client} {StuID} {UserName}" %dir)
    #查看server的命令历史
    elif argv_list[0][1].lower() == "server":
		#目录存在说明学号正确
		if os.path.exists("/monitor/%ss" %argv_list[0][2]) == 1:
			#文件存在说明用户名正确
			if os.path.exists("/monitor/%ss/history_%s" %(argv_list[0][2],argv_list[0][3])) == 1:
				filepath = "/monitor/"+argv_list[0][2]+"s/history_"+argv_list[0][3]
				file = open(filepath,"r")
				content = file.readlines()
				length = len(content)
				for i in range(length):
					if i%2 == 0:
						content[i] = time.ctime(float(content[i][1:]))
						print(content[i])
					else:
						print(content[i][0:-1])
			else:
				print("User: %s does not exist or is not logged on this host,no command history!" %argv_list[0][3])
		else:
			print("The Student ID error or does not exist!")
    #查看client的命令历史
    elif argv_list[0][1].lower() == "client":
		#目录存在说明学号正确
		if os.path.exists("/monitor/%sc" %argv_list[0][2]) == 1:
			#文件存在说明用户名正确
			if os.path.exists("/monitor/%sc/history_%s" %(argv_list[0][2],argv_list[0][3])) == 1:
				filepath = "/monitor/"+argv_list[0][2]+"c/history_"+argv_list[0][3]
				file = open(filepath,"r")
				content = file.readlines()
				length = len(content)
				for i in range(length):
					if i%2 == 0:
						content[i] = time.ctime(float(content[i][1:]))
						print(content[i])
					else:
						print(content[i][0:-1])
			else:
				print("User: %s does not exist or is not logged on this host,no command history!" %argv_list[0][3])
		else:
			print("The Student ID error or does not exist!")
    else:
        print("Parameter is incorrect!")

#定义main函数
def main():
    read_history(sys.argv)

if __name__ == "__main__":
    main()
