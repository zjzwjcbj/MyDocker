#-*- coding: UTF-8 -*-
#!/usr/bin/env python

#导入相关模块
import os
import sys
import xlrd
import commands

#定义读取学生学号信息的函数
def read_excel(abspath):
    #打开文件
    workbook = xlrd.open_workbook(abspath)

    #获取sheet1
    sheet1_name = workbook.sheet_names()[0]

    #根据sheet名称获取sheet内容
    sheet1 = workbook.sheet_by_name(sheet1_name)

    #获取整列的值（数组）
    cols = sheet1.col_values(0)
    return sheet1.nrows,cols

#定义批量删除服务端容器的函数
def del_server_contain(*argv_list):
	#判断传入参数数目是否符合要求
	if len(argv_list[0]) != 2:
		print("Usage: mydocker --bdelsrv {Path-to-File}")
	else:
		#将文件路径规范化为绝对路径
		if argv_list[0][1][0] != "/":
			abspath=os.path.abspath(argv_list[0][1])
		else:
			abspath=argv_list[0][1]
		extension=os.path.splitext(os.path.split(abspath)[-1])[-1]
		if os.path.exists(abspath) and (extension == ".xls" or extension == ".xlsx"):
			#读取学生信息
			(snum,sno_list) = read_excel(abspath)
			print("Get information about %d students,Start removing the Server Container..." %snum)

			#删除所有服务端容器
			num = 0
			failednum = 0
			for sno in sno_list:
				(status,output) = commands.getstatusoutput("docker stop %ss && docker rm %ss" %(sno,sno))
				if status != 0:
					print("%d.The Server Container:%ss does not exist or has been deleted" %(num+1,sno))
					failednum = failednum + 1
				else:
					os.system("rm -rf /workspace/%ss /monitor/%ss" %(sno,sno))
					print("%d.The Server Container:%ss successfully removed" %(num+1,sno))
				num = num + 1
			print("There are %d Server Container successfully removed" %(num-failednum))
		else:
			print("cannot access %s: No such file or directory or Not a excel file" %abspath)

#定义main函数
def main():
    del_server_contain(sys.argv)

if __name__ == "__main__":
    main()
