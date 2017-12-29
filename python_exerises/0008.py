# 第 0008 题： 一个HTML文件，找出里面的正文。

from bs4 import BeautifulSoup

def getHtmlContent(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text()
        
    return content
    

if __name__ == '__main__':
    getHtmlContent(index.html)