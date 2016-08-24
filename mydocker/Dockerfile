#基于centos:latest镜像构建
FROM centos:latest

#邮箱
MAINTAINER from 379148058@qq.com

#安装必要的组件和创建相应的文件
RUN yum install openssh-server openssh-clients vim net-tools gcc gdb lrzsz sudo -y
RUN mkdir -p /var/run/sshd

#创建默认用户并设置密码
RUN useradd admin
RUN echo admin | passwd --stdin admin
RUN echo "admin  ALL=(root) /usr/bin/yum" >> /etc/sudoers
RUN echo root | passwd --stdin root

#设置时间同步
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#添加unp头文件
ADD unpe/libunp.a /usr/lib/
ADD unpe/libunp.a /usr/lib64/
ADD unpe/unp.h /usr/include/
ADD unpe/config.h /usr/include/

#设置记录用户登录信息&&登录后显示本机IP地址
RUN touch /var/log/lastlog && chmod 644 /var/log/lastlog
RUN mkdir /.shell && chmod 555 /.shell
ADD showip.sh /.shell/showip.sh
RUN chmod 444 /.shell/showip.sh && echo "sh /.shell/showip.sh" >> /etc/bashrc
ADD lastlog.sh /.shell/lastlog.sh
RUN chmod 444 /.shell/lastlog.sh && echo "sh /.shell/lastlog.sh" >> /etc/bashrc
ADD collect_cfile.sh /.shell/collect_cfile.sh
RUN chmod 444 /.shell/collect_cfile.sh && echo "sh /.shell/collect_cfile.sh" >> /home/admin/.bash_logout

#设置记录用户历史命令
ADD profile /tmp/profile
RUN cat /tmp/profile >> /etc/profile && rm -rf /tmp/profile

#配置vi&vim环境
ADD virc_vimrc /opt/
RUN cat /opt/virc_vimrc >> /etc/virc && cat /opt/virc_vimrc >> /etc/vimrc && rm -rf /opt/virc_vimrc

#配置ssh服务
ADD ssh_host_rsa_key /etc/ssh/ssh_host_rsa_key
ADD ssh_host_rsa_key.pub /etc/ssh/ssh_host_rsa_key.pub
RUN chmod 600 /etc/ssh/ssh_host_rsa_key
RUN sed -i 's/^HostKey \/etc\/ssh\/ssh_host_ecdsa_key$/#HostKey\ \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config
RUN sed -i 's/^HostKey \/etc\/ssh\/ssh_host_ed25519_key$/#HostKey\ \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config
RUN sed -i -r 's/^(.*pam_nologin.so)/#\1/' /etc/pam.d/sshd

#添加SSH服务启动脚本
ADD run.sh /.run.sh
RUN chmod 755 /.run.sh

#修改ping可执行文件权限
RUN chmod u+s /usr/bin/ping

#设置开放端口
EXPOSE 22

#设置自启动命令
CMD ["/.run.sh"]
