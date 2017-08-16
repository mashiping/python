#!/usr/bin/python
# -*- coding:utf8 -*-

import os,sys,re,urllib,urlparse
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):
    '''''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
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
    @使用attach向MIMEMultipart中追加对象
    '''
    
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
    fromaddr = "xxxxxxx@163.com"  
    smtpaddr = "smtp.163.com"  
    toaddrs = ["11111111@qq.com","xxxxxxxx@xxx.com"]  
    subject = "测试邮件"  
    password = "xxxxxxxxxx"  
    msg = "测试一下"  
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)
