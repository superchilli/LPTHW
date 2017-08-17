#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# def get_pascal_triangle2(n):
#     list = [1]
#     while n > 0:
#         yield list
#         list = [1] + [x + y for x, y in zip(list[:], list[1:])] + [1]
#         n -= 1
#     return
#
#
# for x in get_pascal_triangle2(5):
#     print x

# def normalize(name):
#     new_name = name[0].upper() + name[1:].lower()
#     return new_name
#
# s = map(normalize, ['adam', 'LISA', 'barT', 'thoMaS', 'ROse'])
#
# print (list(s))

# from functools import reduce
#
# def prod(L):
#     def mul(x, y):
#         m = x * y
#         return m
#     return reduce(mul, L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# # 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(s):
#


# 从这个页面：http://photo.weibo.com/5824051112/albums/detail/album_id/4051960286533694?prel=p5_face#!/mode/1/page/3
# 先获取整个页面的源代码
# 再从源代码里获取图片链接
# 下载图片
# 重命名图片

# 下载图片 重命名图片
# import urllib.request
#
# with open('imgurl') as f:
#     for index, line in enumerate(f.readlines()):
#         url = (line.strip())
#         urllib.request.urlretrieve(url, str(index) + '.png')




# from PIL import Image
# import glob
#
#
# for index, infile in enumerate(glob.glob("/Users/rose/emmm/*.png")): # 遍历文件夹的png图片
#         im = Image.open(infile) # 打开图片
#         if im.size[0] > im.size[1]: # 判断长宽，如果长大于宽
#             new_size = (512, 512 * im.size[1] / im.size[0]) # 新尺寸为512， x
#         else:
#             new_size = (512 * im.size[0] / im.size[1], 512) # 反之则 x, 512
#         goodImg = im.resize(new_size) # resize the image
#         goodImg.save("/Users/rose/emmm/" + str(index) + ".png") # rename the image

# 把某一个 URL 对应的 html 正文保存到本地
# 然后找到所有的 URL 执行相同的操作。
# 封装成pdf

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import pdfkit

def parse_url_to_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(reponse.content, "html.parser")
    body = soup.find_all(class_= "x-wki-content")[0]
    html = str(body)
    with open('a.html', 'wb') as f:
        f.write(html)

def get_url_list():
    response = requests.get("https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls

def save_pdf(htmls):
    options = {
    'page-size': 'Letters',
    'encodeing': 'UTF-8',
    'customer-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmls, file_name, options=options)

save_pdf(htmls)
