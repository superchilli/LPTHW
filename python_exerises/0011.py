# coding=utf-8
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

'''
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''

def sensitiveWord(path):
    type_in = input('>>>')
    sens = []
    with open(path) as f:
        for line in f.readlines():
            sens.append(line.strip())
            
    if type_in in sens:
        print('Freedome')
    else:
        print('Human Rights')
        
        
if __name__ == '__main__':
    sensitiveWord('filter.txt')