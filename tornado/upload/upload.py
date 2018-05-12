# -*-coding: utf-8 -*-
"""
UploadHandler类get,post请求实现
"""
import os

import json
import re

import urls
from tools.uploader import Uploader


class Upload(object):
    """
    UploadHandler类get,post请求实现
    """
    def entry_get(self, request):
        """
        处理get请求
        初始化ueditor，返回ueditor配置项
        """
        action = request.get_argument('action', None)
        if action == "config":
            ueditor_config = self._get_config()
            return json.dumps(ueditor_config, ensure_ascii=False)
        return {"error": "initialise fail"} 

    def entry_post(self, request):
        """
        处理post请求
        接收图片的上传
        """
        result = {}
        action = request.get_argument('action', None)
        if action == "uploadimage":
            ueditor_config = self._get_config()
            field_name = ueditor_config.get('imageFieldName')
            config = {
                "pathFormat": ueditor_config['imagePathFormat'],
                "maxSize": ueditor_config['imageMaxSize'],
                "allowFiles": ueditor_config['imageAllowFiles']
            }

            if field_name in request.request.files:
                pictures = request.request.files[field_name]
                for picture in pictures:
                    uploader = Uploader(picture, config)
                    result = uploader.get_file_info()
            else:
                result['state'] = '上传接口错误'
        else:
            result['state'] = '上传接口错误'

        return json.dumps(result)

    def _get_config(self):
        """
        处理ueditor下的config.json文件
        返回json格式的配置项
        """
        static_path = urls.SETTINGS["static_path"]
        with open(os.path.join(static_path, 'ueditor', 'php',
                               'config.json')) as f:
            try:
                # 删除`/**/`之间的注释
                ueditor_config = json.loads(re.sub(r'\/\*.*\*\/', '', f.read()))
            except:
                ueditor_config = {}
        return ueditor_config
