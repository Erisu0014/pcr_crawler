# -*- coding: utf-8 -*-
"""
@Time    : 2021/6/21 10:06
@Author  : 物述有栖
@File    : card.py
@DES     : 爬取卡面
"""
from pyquery import PyQuery as pq
import requests

pre_file_path = r'D:\pycharmProjects\pcr-data\card'
pre_url = 'https://redive.estertion.win/card/profile/'
doc = pq(url=pre_url)
for p in doc('span.item').items():
    avatar_url = p('a').attr.href
    global_url = pre_url + p('a').attr.href  # https://redive.estertion.win/card/profile/102161.webp
    # avatar_doc=pq(avatar_url)
    with open(pre_file_path + '\\' + p('a').attr.href, 'ab') as file:  # 保存到本地的文件名
        file.write(requests.get(global_url).content)
