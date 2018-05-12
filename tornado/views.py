# -*-coding: utf-8 -*-
"""
Handler类集合
"""
import tornado.web

from upload.upload import Upload
from getdata.get_data import GetData
from admin.publish import Publish


class BaseHandler(tornado.web.RequestHandler):
    """
    大多数handler类的基类
    """
    pass


class IndexHandler(tornado.web.RequestHandler):
    """
    接收"/"的请求，渲染首页
    """
    def get(self):
        self.render("index.html")


class ManagerHandler(tornado.web.RequestHandler):
    """
    渲染管理员端页面
    """
    def get(self):
        self.render("manager.html")


class UploadHandler(BaseHandler):
    """
    接收"/upload/"请求，处理文件上传，目前只实现图片上传
    """
    def get(self):
        """
        处理ueditor初始化时的请求
        """
        self.finish(Upload().entry_get(self))

    def post(self):
        """
        处理ueditor上传请求
        """
        self.finish(Upload().entry_post(self))


class GetDataHandler(BaseHandler):
    """
    处理所有以/getdata访问的请求
    根据请求参数key的值，返回不同类型的数据
    """
    def get(self):
        """
        根据请求参数key，返回不同类型数据
        """
        self.finish(GetData().entry_get(self))


class PublishHandler(BaseHandler):
    """
    处理所有以/postdata开头的请求
    """
    def post(self):
        """
        发布信息
        """
        self.finish(Publish().entry_post(self))

