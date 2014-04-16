#!/bin/env python
# -*- coding:utf8 -*-

from handlers import home

handlers = [
    (r'/', home.IndexHandler),
]
