#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

# 1. open the image
# 2. get a font
# 3. get a color
# 4. draw the string at the given position

from PIL import ImageDraw, Image, ImageFont

def add_num(img):
    draw = ImageDraw.ImageDraw(img)
    width, height=img.size
    fontSize = min(width, height) // 10
    fnt = ImageFont.truetype('Arial.tff', fontSize)
    color = (255,0,0)
    draw.text((0.9*width, 0.1*height), "1", fill=color, font=fnt)
    img.save('avatar.jpg', 'jpeg')
    return

image = Image.open('/123.jpg')
add_num(image)