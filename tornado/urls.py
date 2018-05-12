# -*-coding: utf-8 -*-
"""
url配置
"""
import os

import tornado.web

from views import (IndexHandler, UploadHandler, GetDataHandler,
                   PublishHandler, ManagerHandler)

SETTINGS = {
    "debug": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

HANDLES = {
    (r"/", IndexHandler),
    (r"/upload/", UploadHandler),
    (r"/getdata", GetDataHandler),
    (r"/postdata", PublishHandler),
    (r"/lab_web/manger_page", ManagerHandler)
}

application = tornado.web.Application(
    handlers=HANDLES,
    **SETTINGS
)