#!/usr/bin/python
# -*- coding: utf-8 -*-
# "删除指定目录一天前的文件“

import os
import time
import re

def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            re_name = re.match(r'(%s).*' % daytime,name)
            if re_name is None:
                os.remove(os.path.join(root, name))
            #   print 'file_name:',name

if __name__ == "__main__":
    path = '/var/cron/zyl/test'
    daytime = str(time.strftime("%Y-%m-%d", time.localtime()))
    del_files(path)
