# -*- coding: utf-8 -*-
"""
@Time    : 2021/6/21 8:57
@Author  : 物述有栖
@File    : avatar.py
@DES     : 用以设置对应关系
"""
from pyquery import PyQuery as pq
from selenium import webdriver

pre_url = 'https://redive.estertion.win/icon/unit/'

driver = webdriver.Chrome(executable_path="D:\pycharmProjects\pcr-data\chromedriver.exe")
driver.get(pre_url)
elements = driver.find_elements_by_class_name('item')

for e in elements:
    href = e.find_element_by_tag_name('a').get_attribute('href')
    name = e.text.split('\n')[0]
    if not name.isdigit():
        print(e.text.split('\n')[0] + "\t" + href.split('/')[-1])
# avatar_url = p('a').attr.href
# global_url = pre_url + p('a').attr.href  # https://redive.estertion.win/icon/unit/100111.webp
# print(global_url)
# avatar_doc=pq(avatar_url)
