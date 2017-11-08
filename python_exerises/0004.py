# -*- coding: utf-8 -*-
# 任一个英文的纯文本文件，统计其中的单词出现的个数。

import collections


with open('text.txt','r') as f:
    words = f.read().split(" ")

cnt = collections.Counter()
for i in words:
    cnt[i] += 1

print cnt
