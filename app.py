#!/usr/bin/env python
#!-*- coding:utf8 -*-

import os.path

from tornado.web import RequestHandler, Application
from tornado.options import define, options, parse_command_line
from tornado.ioloop import IOLoop

import routes

class App(Application):
    def __init__(self):
        basePath = os.path.dirname(__file__)
        setting = dict(
            template_path = os.path.join(basePath, "template"),
            static_path = os.path.join(basePath, "static"),
            debug = True,
        )
        super(App, self).__init__(routes.handlers, **setting)

def main():
    define('port', default=8888, help='Run on the given port.')
    
    #---------- 日志
    options.log_file_prefix = os.path.join(os.path.dirname(__file__), 'logs/web.log')
    options.log_file_max_size = 10 * 1000 * 2014
    options.logging = 'debug'

    parse_command_line();
    
    app = App()
    app.listen(options.port)
    print('App start on port: %s' % options.port)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()
