#!/bin/bash
#收集C程序文件并复制到/home/admin/workspace

find / -path "/home/admin/workspace" -prune -o -name "*.c" -exec cp -r {} /home/admin/workspace/ \; 2> /dev/null
