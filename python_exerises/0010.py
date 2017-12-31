# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def rndChr():
    return chr(random.randiant(65, 90))
    
def rndColor():
    return (random.randiant(64, 255), random.randiant(64, 255), random.randiant(64, 255))
    
def rndColor2():
    return (random.randiant(32, 127), random.randiant(32, 127), random.randiant(32, 127))
    
def compose():
    width = 240
    hight = 60
    im = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('arial.ttf', 36)
    draw = ImageDraw.draw(im)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
            
    letter = []
    for t in range(4):
        letter.append(rndChr())
        draw.text((60*t+10, 10), letter[t], font=font, fill=rndColor2())
        
    im.save('rndcode.jpg', 'jpeg')
    im = im.filter(ImageFilter.BLUR)
    im.save('blurcode.jpg', 'jpeg')
    
    print(letter)
    
if __name__ == '__main__':
    compose()