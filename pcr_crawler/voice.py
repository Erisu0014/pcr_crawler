# -*- coding: utf-8 -*-
"""
@Time    : 2021/1/11 15:14
@Author  : 物述有栖
@File    : voice.py
@DES     : 我爬我爬_音频
"""
from pyquery import PyQuery as pq
import os
import time
import requests
import random

pre_file_path = r'D:\pycharmProjects\pcr-data\audio'
pre_url = 'https://redive.estertion.win/sound/'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

random_agent = USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)]
headers = {
    'User-Agent': random_agent
}

doc = pq(url=pre_url)
for p in doc('pre a').items():
    type_url = pre_url + p.attr.href
    if type_url.find('..') != -1 or "vo_btg" not in type_url:  # https://redive.estertion.win/sound/story_vo/../
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
            # 不存在文件夹，创建文件夹
            if not os.path.exists(pre_file_path + '\\' + num_url.split('/')[-2]):
                os.makedirs(pre_file_path + '\\' + num_url.split('/')[-2])
            file_path = pre_file_path + '\\' + num_url.split('/')[-2] + '\\' + m4a_doc.attr.href
            print(file_path)
            if os.path.exists(file_path):
                continue
            with open(file_path, 'ab') as file:  # 保存到本地的文件名
                file.write(requests.get(url=m4a_url, headers=headers).content)
            file.close()
            # time.sleep(2)
