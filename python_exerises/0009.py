# 第 0009 题： 一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup

def findLink(filepath):
    allLink = []
    with open(filepath) as f:
        content = f.read()
        soup = BeautifulSoup(content)
        
        for link in soup.find_all('a'):
            allLink.append(link.get('href'))
    
    return allLink
    
    
if __name__ == '__main__':
    findLink('index.html')