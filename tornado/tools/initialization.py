# -*-coding: utf-8 -*-
"""
改变环境时首先运行的脚本
内容包括：
1.初始化数据库
"""
from peewee import CharField, Model, MySQLDatabase, TextField, CompositeKey

db = MySQLDatabase(host='127.0.0.1', user='root', passwd='123456',
                   database='lab_web')


class MyBaseModel(Model):
    class Meta:
        database = db


class main_data(MyBaseModel):
    """
    数据库只有唯一一个表
    表拥有两个属性
    1.name 标识属性的类型及id
    2.text 存放各类处理过的html文本
    """
    name_id = CharField(null=False, unique=True)
    html_content = TextField(null=False)


db.connect()
db.create_table(main_data, safe=True)
db.close()
print('mysql initalise success!!!')
