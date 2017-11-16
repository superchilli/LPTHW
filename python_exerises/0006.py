# -*- coding: utf-8 -*-
# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# 1. 确认日记路径
# 2. 匹配符合的日记，并获取文件和文件内容
# 3. 去除常用介词
# 4. 获取单词出现次数
# 5. 打印频率最高的词

import os
import re

def findWord(dirPath):
    if not os.path.isdir(dirPath):
        return
    fileList = os.listdir(dirPath)
    reObj = re.compile('\d?(\w+)\d?')
    for file in fileList:
        filePath = os.path.join(dirPath, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt':
            with open(filePath) as f:
                data = f.read()
                words = reObj.findall(data)
                wordDict = dict()
                for word in words:
                    word = word.lower()
                    if word in ['a', 'the', 'to']:
                        continue
                    if word in wordDict:
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
            anaList = sorted(wordDict.items(), key = lambda t:t[1], reverse=True)
            print('the most popular word is: %s' % (anaList[0][0]))


if __name__ == '__main__':
    findWord('0006/diary')