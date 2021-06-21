# -*- coding: utf-8 -*-
"""
@Time    : 2021/6/21 8:57
@Author  : 物述有栖
@File    : avatar.py
@DES     : 爬取人物
"""
from pyquery import PyQuery as pq
import requests

pre_file_path = r'D:\pycharmProjects\pcr-data\avatar'
pre_url = 'https://redive.estertion.win/icon/unit/'
doc = pq(url=pre_url)
for p in doc('span.item').items():
    avatar_url = p('a').attr.href
    global_url = pre_url + p('a').attr.href  # https://redive.estertion.win/icon/unit/100111.webp
    # avatar_doc=pq(avatar_url)
    with open(pre_file_path + '\\' + p('a').attr.href, 'ab') as file:  # 保存到本地的文件名
        file.write(requests.get(global_url).content)
