#!/bin/bash
#显示本机IP地址

ip=`ifconfig eth0 |grep 'inet' |awk '{print $2}' | grep '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'`
echo "Your IP Address is:$ip"
