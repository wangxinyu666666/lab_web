# -*- coding: utf-8 -*-
"""
管理员发布信息的请求处理
"""
import json
import re
import datetime
import ast

from orm import main_data, db


class Publish(object):
    """
    处理以/postdata开头的请求
    """
    def entry_post(self, request):
        """
        post函数的入口
        根据key值不同进入不同分支
        """
        key = request.get_argument('key', None)
        body = request.request.body.decode()
        if body:
            body = ast.literal_eval(body)
            if 'HTML' in body:
                html_data = body['HTML']  
        if not key:
            result = {'error': 'missing value key'}
        if key == 'add_news':
            result = self._add_news_or_notice('news', html_data)
        elif key == 'add_notice':
            result = self._add_news_or_notice('notice', html_data)
        elif key == 'intro':
            result = self._rewrite_introduce_of_center(html_data)
        elif key in ('index_imgs_html', 'enviro_imgs_html'):
            result = self._rewrite_images_html(key, html_data)
        elif key in ('projects', 'union', 'friends', 'gains', 'patent',
                     'article', 'soft'):
            result = self._rewrite_science_data(key, html_data)
        elif key.startswith('news') or key.startswith('notice'):
            result = self._rewrite_news_or_notice(key, html_data)
        elif key.startswith('rewrite_'):
            result = self._rewrite_overview_or_detail_data(key, html_data)
        elif key.startswith('delete_'):
            result = self._delete_data(key)
        elif key.startswith('add_'):
            result = self._add_data(key, html_data)
        elif key.startswith('lab_'):
            result = self._set_lab_data(key, html_data)

        return json.dumps(result, ensure_ascii=False)

    def _set_lab_data(self, key, html):
        """添加或修改组织机构的信息

        key值为固定四个值之一
        """
        with db.execution_context():
            data = main_data.select().where(main_data.name_id == key)
        if not data:
            # 第一次插入
            with db.execution_context():
                main_data.create(**{'name_id': key,
                                    'html_content': html})
        else:
            # 更新
            with db.execution_context():
                main_data.update(**{'html_content': html}).where(
                    main_data.name_id == key).execute()
        return {'state': 'SUCCESS'}

    def _add_data(self, key, html):
        """在数据库中添加一条记录

        根据key值的不同选择不同的前缀+时间戳形成name_id字段
        """
        now = datetime.datetime.now()
        time = now.strftime('%y%m%d%H%M%S')
        pre_name = key.split('_')[1]
        name = pre_name + '_' + time
        detail_name = 'desc_' + name
        pictures = re.findall(r'src="(.*?)"', html)
        if not pictures or len(pictures) > 1:
            return {'error': '照片数量必须为1'}
        with db.execution_context():
            # 插入概览信息
            main_data.create(**{'name_id': name,
                                'html_content': html})
            main_data.create(**{'name_id': detail_name,
                                'html_content': ''})
        return {'state': 'SUCCESS'}

    def _delete_data(self, key):
        """从数据库中删除一条记录

        根据key值delete_之后name_id删除
        """
        name = key[7:]
        detail_name = 'desc_' + name
        with db.execution_context():
            # 删除概览记录
            main_data.delete().where(main_data.name_id == name).execute()
            # 删除详细记录
            main_data.delete().where(main_data.name_id == detail_name) \
                              .execute()
        return {'state': 'SUCCESS'}

    def _rewrite_overview_or_detail_data(self, key, html):
        """修改概览信息或者详细信息

        提取key值中的name_id字段
        """
        name = key[8:]
        if 'desc_' not in name:
            # 修改概览信息
            pictures = re.findall(r'src="(.*?)"', html)
            if not pictures or len(pictures) > 1:
                return {'error': '照片数量必须为1'}
        with db.execution_context():
            main_data.update(**{'html_content': html}).where(
                main_data.name_id == name).execute()
        return {'state': 'SUCCESS'}

    def _add_news_or_notice(self, key, html):
        """
        添加新闻或通知
        """
        title = re.findall(r'<h1(.*?)</h1>', html)
        if not title:
            return {'error': '缺少一个标题'}
        elif len(title) >= 2:
            return {'error': '标题数目大于一个'}

        now = datetime.datetime.now()
        time = now.strftime('%y%m%d%H%M%S')

        name = key + '_' + time

        with db.execution_context():
            main_data.create(**{"name_id": name,
                                "html_content": html})
        return {'state': 'SUCCESS'}

    def _rewrite_news_or_notice(self, key, html):
        """
        修改新闻或通知
        """
        title = re.findall(r'<h1>(.*?)</h1>', html)
        if not title:
            return {'error': '缺少一个标题'}
        elif len(title) >= 2:
            return {'error': '标题数目大于一个'}

        with db.execution_context():
            main_data.update(**{"html_content": html}) \
                    .where(main_data.name_id == key).execute()
        return {'state': 'SUCCESS'}

    def _rewrite_images_html(self, key, html):
        """修改首页走马灯或者中心环境图片

        key值为'index_imgs_html'或'enviro_imgs_html'
        """
        return self._rewrite_html(key, html)

    def _rewrite_science_data(self, key, html):
        """修改科学研究板块的内容

        包括科研项目projects,联合实验室union,合作伙伴friends,系统证书gains,
        专利patent,论文article,软著soft
        key值为'projects', 'union', 'friends', 'gains', 'patent', 'article',
        'soft'
        """
        return self._rewrite_html(key, html)

    def _rewrite_introduce_of_center(self, html):
        """
        修改中心简介
        """
        return self._rewrite_html('intro', html)

    def _rewrite_html(self, key, html):
        """修改html内容
        """
        with db.execution_context():
            html_content = main_data.select().where(main_data.name_id == key)
        if not html_content:
            # 第一次添加
            with db.execution_context():
                main_data.create(**{"name_id": key, "html_content": html})
        else:
            with db.execution_context():
                main_data.update(**{"html_content": html}).where(
                    main_data.name_id == key).execute()
        return {"state": "SUCCESS"}
