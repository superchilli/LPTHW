import re
import os
import urllib.request

from bs4 import BeautifulSoup

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
    
    
def getAllImg(html):
    soup = BeautifulSoup(html)
    imgTags = soup.find_all('img')
    imgLists = []
    for link in imgTags:
        imgLists.append(link.get('src'))
    return imgLists
    
    
def mkdir(path):
    path=path.strip()
    isExist=os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        return True
    else:
        return False
        
def saveImgs(imgLists, name):
    number = 1
    for imgUrl in imgLists:
        splitPath = imgUrl.split('.')
        ext = ['jpg', 'gif', 'png', 'jpeg']
        fTail = splitPath.pop()
        if len(fTail) > 3 or fTail not in ext:
            fTail = 'jpg'
        fileName = name + '/' + str(number) + '.' + fTail
        
        try:
            u = urllib.request.urlopen(imgUrl)
            data = u.read()
            with open(fileName, 'wb+') as f:
                f.write(data)
        except urllib.error.URLError as e:
            print(e.reason)
        number += 1
        
if __name__ == "__main__":
    html = getHtml('https://book.douban.com/')
    path = 'img'
    mkdir(path)
    imgLists = getAllImg(html)
    saveImgs(imgLists,path)

