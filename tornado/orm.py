# -*-coding: utf-8 -*-
from peewee import CharField, Model, TextField, CompositeKey
from playhouse.shortcuts import model_to_dict
from playhouse.pool import PooledMySQLDatabase


try:
    db = PooledMySQLDatabase(
        database='lab_web',
        max_connections=4,
        stale_timeout=3600,
        timeout=0,
        user='root',
        host='127.0.0.1',
        passwd='123456'
    )
    with db.execution_context():
        pass
except Exception as e:
    print("mysql error:" + e)

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

