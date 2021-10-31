FROM centos:latest

LABEL maintainer="Anish Khandelwal <anishkhandelwal.1999@gmail.com>"

RUN yum install httpd -y

COPY index.html /var/www/html

CMD /usr/sbin/httpd $OPTIONS -DFOREGROUND

EXPOSE 80 

