#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-01-17 13:45:07
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

import os
import sys

# 这里修改为您的项目名称，其它的不要变
PROJECT_NAME = 'zqxt'


os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings'%PROJECT_NAME

path = os.path.dirname(os.path.abspath(__file__)) + '/%s'%PROJECT_NAME
if path not in sys.path:
    sys.path.insert(1, path)

from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
 
application = WSGIApplication(WSGIHandler())