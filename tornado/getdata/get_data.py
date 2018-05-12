# -*-coding: utf-8 -*-
"""
处理以/getdata开头的请求
包括首页走马灯，新闻，通知
"""
import json
import re

from orm import main_data, model_to_dict, db


class GetData(object):
    """
    处理以/getdata开头的请求
    """
    def entry_get(self, request):
        """
        get请求的入口
        根据key的值，进入不同分支
        """
        key = request.get_argument('key', None)
        if not key:
            return {'error': 'missing value key'}
        if key in ('news', 'notice', 'intro'):
            if key == 'news':  # 获取新闻列表或单条新闻详情
                result = self._get_news_or_notice(key)
            elif key == 'notice':  # 获取通知列表或单条通知详情
                result = self._get_news_or_notice(key)
            elif key == 'intro':  # 获取中心简介
                result = self._get_introduce_of_center()
        elif key in ('leaders', 'teachers', 'jishi', 'happy'):
            result = self._get_all_overview_data(key)
        elif key in ('index_imgs', 'enviro_imgs'):
            result = self._get_images(key)
        elif key in ('index_imgs_html', 'enviro_imgs_html'):
            result = self._get_images_html(key)
        elif key in ('projects', 'union', 'friends'):
            result = self._get_science_data(key)
        elif key in ('gains', 'patent', 'article', 'soft'):
            result = self._get_science_result_data(key)
        else:
            pre_key = key.split('_')[0]
            if pre_key in ('news', 'notice'):
                result = self._get_news_or_notice(key)
            elif pre_key == 'desc' or pre_key == 'lab':
                result = self._get_detail_data(key)

        return json.dumps(result, ensure_ascii=False)

    def _get_science_result_data(self, key):
        """返回科研成果html内容

        分为系统证书，专利，论文，软著
        ('gains', 'patent', 'article', 'soft')
        """
        with db.execution_context():
            data = main_data.select(main_data.html_content).where(
                main_data.name_id == key)
        return {'HTML': data[0].html_content}

    def _get_all_overview_data(self, key):
        """返回所有概览信息

        可能的类别有领导，教师，纪实活动，欢乐时光
        数据格式{"getdata": [{"pictures": "src",
                             "html": "xxxxx",
                             "name": "overviews_xxxxx"},
                             {"pictures": "src",
                              "html": "xxxxxx",
                              "name": "overviews_xxxxx"}]}
        """
        if key == 'leaders':
            name = 'leader'
        elif key == 'teachers':
            name = 'teacher'
        else:
            name = key
        with db.execution_context():
            overviews = main_data.select(main_data.name_id,
                                         main_data.html_content) \
                               .where(main_data.name_id.startswith(name))
        data_list = []
        for overview in overviews:
            overview = model_to_dict(overview)
            edit = overview['html_content']
            pictures = re.findall(r'src="(.*?)"', overview['html_content'])
            pictures = pictures[0]
            html = re.sub(r'<img.*?>', '', overview['html_content'])
            data_list.append({"pictures": pictures,
                              "html": html,
                              "name": overview['name_id'],
                              "edit": edit})
        return {"getdata": data_list}

    def _get_introduce_of_center(self):
        """返回中心简介
        """
        return self._get_html_data('intro')

    def _get_news_or_notice(self, key):
        """
        返回新闻或通知
        key不带Id时返回所有的新闻或通知
        key为指定id值时返回具体新闻或通知内容
        """
        # 返回所有新闻的名字，时间，和对应id
        if key in ('news', 'notice'):
            with db.execution_context():
                all_data = main_data.select(main_data.name_id,
                                            main_data.html_content). \
                                    where(main_data.name_id.startswith(key))
            data_list = []
            for data in all_data:
                data = model_to_dict(data)
                title = self._get_title(data['html_content'])
                time = self._get_time(data['name_id'])
                news_id = data['name_id']
                data_list.append({
                    'name': title,
                    'time': time,
                    'id': news_id
                })

            return {'data': data_list}
        else:
            # 带具体值时返回新闻具体内容
            with db.execution_context():
                single_data = main_data.select(main_data.html_content) \
                                    .where(main_data.name_id == key)
            return {'HTML': str(single_data[0].html_content)}

    def _get_images(self, key):
        """提取html中所有图片的src

        html为首页走马灯或中心环境的html内容
        key值为'index_imgs'或'enviro_imgs'
        json:{'pictures': ['url_1', 'url_2', 'url_3']}
        """
        name = key + '_html'
        with db.execution_context():
            html_data = main_data.select(main_data.html_content) \
                                .where(main_data.name_id == name)
        html_data = model_to_dict(html_data[0])
        src = re.findall(r'src="(.*?)"', html_data["html_content"])
        return {'pictures': src}

    def _get_images_html(self, key):
        """返回首页走马灯图片或中心环境图片的html内容

        key值为'index_imgs_html'或'enviro_imgs_html'
        """
        return self._get_html_data(key)

    def _get_science_data(self, key):
        """返回科学研究板块的html内容

        key值为('projects', 'union', 'friends')中一个
        """
        return self._get_html_data(key)

    def _get_detail_data(self, key):
        """返回指定中心领导或实验室的详细信息

        return: {"HTML": "xxxxxxxx"}
        """
        return self._get_html_data(key)

    def _get_html_data(self, key):
        """返回key值对应的html_content内容
        """
        with db.execution_context():
            data = main_data.select(main_data.html_content).where(
                main_data.name_id == key)
        if not data:
            return {'error': 'no data'}
        return {'HTML': str(data[0].html_content)}

    def _get_title(self, html_data):
        """
        从新闻或通知中提取出标题
        """
        data = re.findall(r'<h1(.*?)>(.*?)</h1>', html_data)
        title = data[0][1]
        title = re.sub(r'<.*?>', '', title)
        return str(title)

    def _get_time(self, name_id):
        """
        从name_id中提取出id里的时间戳，格式为yy-mm-dd
        """
        number = name_id.split('_')[-1]
        year = str(number[:2])
        month = str(number[2:4])
        day = str(number[4:6])
        return '-'.join([year, month, day])
