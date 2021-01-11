# -*- coding: utf-8 -*-
"""
@Time    : 2021/1/11 15:14
@Author  : 物述有栖
@File    : voice.py
@DES     : 我爬我爬_音频
"""
from pyquery import PyQuery as pq
import requests

pre_file_path = r'D:\pycharmProjects\pcr-data\audio\\'
pre_url = 'https://redive.estertion.win/sound/'
doc = pq(url=pre_url)
for p in doc('pre a').items():
    type_url = pre_url + p.attr.href
    if type_url.find('..') != -1:  # https://redive.estertion.win/sound/story_vo/../
        continue
    type_doc = pq(url=type_url)  # https://redive.estertion.win/sound/story_vo/
    for num_doc in type_doc('pre a').items():
        num_url = type_url + num_doc.attr.href  # https://redive.estertion.win/sound/story_vo/0000011/
        if num_url.find('..') != -1:  # https://redive.estertion.win/sound/story_vo/../
            continue
        vo_doc = pq(url=num_url)
        for m4a_doc in vo_doc('pre a').items():
            m4a_url = num_url + m4a_doc.attr.href
            if m4a_url.find('..') != -1:  # https://redive.estertion.win/sound/story_vo/../
                continue
            with open(pre_file_path + m4a_doc.attr.href, 'ab') as file:  # 保存到本地的文件名
                file.write(requests.get(m4a_url).content)
                file.flush()
