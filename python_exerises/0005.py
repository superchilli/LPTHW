# -*- coding: utf-8 -*-
# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os

path = '0005/image'
resultPath = '0005/result'

if not os.path.isdir(resultPath):
    os.mkdir(resultPath)

for pic in os.listdir(path):
    picPath = os.path.join(path, pic)
    with Image.open(picPath) as im:
        w, h = im.size
        r = w / 1366 if (w / 1366) >= (h / 640) else h / 640
        newSize = w / n, h/n
        im.thumbnail(newSize)
        im.save(resultPath + pic.split('.')[0] + '.jpg', 'jpeg')

