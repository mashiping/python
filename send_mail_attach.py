#!/usr/bin/python
# -*- coding:utf8 -*-

import os,sys,re,urllib,urlparse
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password,filename):
    '''''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    @filename:附件名称
    '''
    mail_msg = MIMEMultipart()
    '''
    @创建MIMEMultipart
    '''
    if not isinstance(subject,unicode):
        subject = unicode(subject, 'utf-8')
    mail_msg['Subject'] = subject
    mail_msg['From'] =fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    '''
    @上面是使用attach向MIMEMultipart中追加对象msg
    '''
    '''
    @添加附件“a.txt”
    '''
    att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="a.txt"'
    mail_msg.attach(att)
    
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)
        s.login(fromaddr,password)
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string())
        s.quit()
    except:
        print "Error: unable to send email"
        print traceback.format_exc()

if __name__ == '__main__':
    fromaddr = "xxxxxxxxxx@163.com"  
    smtpaddr = "smtp.163.com"  
    toaddrs = ["11111111@qq.com","xxxxxx@xxx.com"]  
    subject = "测试邮件"  
    password = "xxxxxxxxx"  
    msg = "测试一下"  
    filename = "/srv/test/a.txt"
    '''
    @以下是文件内容，验证中文，英文，数字和特殊字符不出乱码

    哈哈，打开看看
    english
    !@#$%^&*()_
    1234567890qwertyuiozxcvZXCVBSDFG<><><L<
    '''
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password,filename)

