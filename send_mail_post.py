#!/usr/bin/python
# -*- coding:utf-8 -*-

import re,os,sys
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
import smtplib, datetime

reload(sys)
sys.setdefaultencoding("utf-8")

class SendMailHandler(RequestHandler):

    def post(self):
        revs = self.get_argument('tos', '', 'utf-8')
        sub = self.get_argument('subject', '', 'utf-8')
        body = self.get_argument('content', '',	'utf-8')
        filename = self.get_argument('filename', '', 'utf-8')
        for rev in revs.split(','):
            ret = self.__do_handle(rev,sub,body,filename)
            self.finish()

    def __do_handle(self,rev,sub,body,filename):
        mail_server = 'smtp.163.com'
        mail_user = 'mashiping2010@163.com'
        mail_pwd = 'Msp196201117'
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = mail_user
        msg['To'] = rev
        msg['Date'] = formatdate() 
        msg.attach(MIMEText(body, 'html', 'utf-8'))
        print "__do_handle msg: %s" % msg

        att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="a.txt"'
        msg.attach(att)

        try:
            session = smtplib.SMTP()
            session.connect(mail_server)
            session.login(mail_user, mail_pwd)
            session.sendmail(mail_user, rev, msg.as_string())
            session.quit()
        except:
            print "Error: unable to send email"
            #print traceback.format_exc()

settings = {}

application = Application([(r"/mail",SendMailHandler),], **settings)

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(6666)
    IOLoop.instance().start()
