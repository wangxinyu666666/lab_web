# -*-coding: utf-8 -*-
"""
将图片上传操作中的图片保存在服务器
"""
import os

import re
import random
import datetime


class Uploader(object):
    """
    对上传的图片做相应的判断后，保存在服务器，并返回该图片的url
    """
    STATE_MAP = [  # 上传状态映射表
        "SUCCESS",  # 上传成功标记，在UEditor中内不可改变，否则flash判断会出错
        "文件大小超出 upload_max_filesize 限制",
        "文件大小超出 MAX_FILE_SIZE 限制",
        "文件未被完整上传",
        "没有文件被上传",
        "上传文件为空",
    ]

    STATE_ERROR = {
        "ERROR_TMP_FILE": "临时文件错误",
        "ERROR_TMP_FILE_NOT_FOUND": "找不到临时文件",
        "ERROR_SIZE_EXCEED": "文件大小超出网站限制",
        "ERROR_TYPE_NOT_ALLOWED": "文件类型不允许",
        "ERROR_CREATE_DIR": "目录创建失败",
        "ERROR_DIR_NOT_WRITEABLE": "目录没有写权限",
        "ERROR_FILE_MOVE": "文件保存时出错",
        "ERROR_FILE_NOT_FOUND": "找不到上传文件",
        "ERROR_WRITE_CONTENT": "写入文件内容错误",
        "ERROR_UNKNOWN": "未知错误",
        "ERROR_DEAD_LINK": "链接不可用",
        "ERROR_HTTP_LINK": "链接不是http链接",
        "ERROR_HTTP_CONTENTTYPE": "链接contentType不正确"
    }

    def __init__(self, fileobj, config):
        """
        :param fileobj: post上传的图片对象
        :param config: 配置信息
        :param static_folder: 图片将要保存的目录
        """
        self._fileobj = fileobj
        self._config = config
        self._static_folder = os.path.join('static')
        self.upload_pic()

    def upload_pic(self):
        """
        上传图片处理方法
        """
        self._original_name = self._fileobj['filename']

        # 获取图片大小
        self._file_size = len(self._fileobj['body'])

        self._file_type = self._get_file_ext()
        self._full_name = self._get_full_name()
        self._file_path = self._get_file_path()

        # 检查图片大小是否超出限制
        if not self._check_size():
            self._state_info = self._get_state_error('ERROR_SIZE_EXCEED')
            return

        # 检查是否是允许的图片格式
        if not self._check_type():
            self._state_info = self._get_state_error('ERROR_TYPE_NOT_ALLOWED')
            return

        # 保存图片
        with open(self._file_path, 'wb') as f:
            f.write(self._fileobj['body'])
            self._state_info = self.STATE_MAP[0]

    def _get_state_error(self, error):
        """
        上传错误检查
        """
        return self.STATE_ERROR.get(error, 'ERROR_UNKNOWN')

    def _get_full_name(self):
        """
        重命名文件
        """
        now = datetime.datetime.now()
        time = now.strftime('%y%m%d%H%M%S')

        # 替换日期事件
        # _format:"/image/{time}{rand:6}"
        _format = self._config['pathFormat']
        _format = _format.replace('{time}', time)

        rand_re = r'\{rand\:(\d*)\}'
        _pattern = re.compile(rand_re, flags=re.I)
        _match = _pattern.search(_format)
        if _match:
            n = int(_match.groups()[0])
            _format = _pattern.sub(str(random.randrange(10**(n-1), 10**n)),
                                   _format)

        _ext = self._get_file_ext()
        return '{}{}'.format(_format, _ext)

    def _get_file_ext(self):
        """
        获取文件扩展名
        """
        return '.{}'.format(self._original_name.split('.')[-1].lower())

    def _get_file_path(self):
        """
        获取文件完整路径
        """
        root_path = self._static_folder
        file_path = ''
        for path in self._full_name.split('/'):
            file_path = os.path.join(file_path, path)
        return os.path.join(root_path, file_path)

    def _check_size(self):
        """
        检查图片大小是否超出限制
        """
        return self._file_size <= self._config['maxSize']

    def _check_type(self):
        """
        检查图片格式是否在允许格式内
        """
        return self._file_type.lower() in self._config['allowFiles']

    def _check_file_type(self):
        """
        文件类型检测
        """
        return self._file_type.lower() in self._config['allowFiles']

    def get_file_info(self):
        """
        获取当前上传成功的图片的各项信息
        """
        return {
            'state': self._state_info,
            'url': "http://39.108.181.155:8020/" + self._file_path,
            'titile': self._original_name,
            'original': self._original_name
        }
