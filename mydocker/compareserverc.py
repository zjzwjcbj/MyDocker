#-*- coding:UTF8 -*-
import os,os.path
import re

#保存所有C程序文件的路径
pathlist = []
lcslist = []

#遍历目录查找C程序文件
def search_c(root,dirs,files):
	global pathlist
	for file in files:
		path = os.path.join(root,file)
		path = os.path.normcase(path)
		if re.search(r"s/.*\.c",path):
			pathlist.append(path)

#求最长公共子序列
def lcs(a,b):
	lena=len(a)
	lenb=len(b)
	c=[[0 for i in range(lenb+1)] for j in range(lena+1)]
	flag=[[0 for i in range(lenb+1)] for j in range(lena+1)]
	for i in range(lena):
		for j in range(lenb):
			if a[i]==b[j]:
				c[i+1][j+1]=c[i][j]+1
				flag[i+1][j+1]='ok'
			elif c[i+1][j]>c[i][j+1]:
				c[i+1][j+1]=c[i+1][j]
				flag[i+1][j+1]='left'
			else:
				c[i+1][j+1]=c[i][j+1]
				flag[i+1][j+1]='up'
	return c,flag

def printLcs(flag,a,i,j):
	global lcslist
	if i==0 or j==0:
		return
	if flag[i][j]=='ok':
		printLcs(flag,a,i-1,j-1)
		lcslist.append(a[i-1])
	elif flag[i][j]=='left':
		printLcs(flag,a,i,j-1)
	else:
		printLcs(flag,a,i-1,j)
	

#比较两个文件的内容并计算重复率
def compare(path1,path2):
	file1 = open(path1)
	file2 = open(path2)

	fa = file1.readlines()
	fb = file2.readlines()

	file1.close()
	file2.close()

	#去除每行中的空格
	fa = [ str.strip() for str in fa ]
	fb = [ str.strip() for str in fb ]

	#去除空行
	content1 = []
	content2 = []

	for i in fa:
		if i == '':
			continue
		content1.append(i)

	for j in fb:
		if j == '':
			continue
		content2.append(j)

	#将文件内容合成一个字符串
	con1 = ''.join(content1)
	con2 = ''.join(content2)

	c,flag=lcs(con1,con2)
	printLcs(flag,con1,len(con1),len(con2))
	percent = (len(lcslist)*2.0)/(len(con1)+len(con2))
	percent = percent * 100
	 
	print("The repetition rate of %s and %s is:%0.2d%%" %(path1,path2,percent))

if __name__ == '__main__':
	for root,dirs,files in os.walk('/workspace'):
		search_c(root,dirs,files)
	if len(pathlist) == 0:
		print("C code file not found!")
	if len(pathlist) == 1:
		print("Only one C file, can not be compared!")
	else:
		for i in range(len(pathlist)-1):
			for j in range(i+1,len(pathlist),1):
				compare(pathlist[i],pathlist[j])
