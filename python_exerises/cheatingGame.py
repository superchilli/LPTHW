#coding:utf-8

# 简介s
# 剧情：做头发

def hairStyle():
    print('''
    ！！！申明：本游戏完全虚构，如有雷同，纯属巧合。！！！
    
    剧情简介：
    露露，女，年龄：37，职业：演员
    
    亮亮，男，年龄：35，职业：演员，和露露关系：老公

    苏苏，女，年龄：37，职业：演员，和露露关系：塑料姐妹，和亮亮关系：朋友，

    屁屁：男，职业：歌手，和亮亮关系：塑料兄弟；和露露关系：不明。

    露露和苏苏都是屁屁的粉丝。
    ''')
    print('''
    一天，9pm，露露对亮亮说，“老公，我去做头发了。”

    亮亮正在带娃，开心地回复老婆，“好的，去吧！我直播一会儿。”

    接着露露出门了，亮亮开始直播。
        ''')

    answer1 = input('''
                A：露露真的去做头发了。
                B：都九点了做什么头发？？？
                你的回答是(A/B): 
                    ''')
    if answer1.lower() == 'a':
        greenHat()
    elif answer1.lower() == 'b':
        elevenClock()
    else:
        print('''
        回答无效，请输入A或者B。''')
        hairStyle()
    
def greenHat():
    print('''
    恭喜你，你通关了，送你一个通关大奖：
    >>> 绿帽子一顶。''')  
    
def playHat():
    print('''
    由于露露禁止你玩游戏，好不容易露露不在家，你试图联系好哥们屁屁一起上线打王者荣耀。
    屁屁打了2把就说累了要睡了，你只好一个人玩到凌晨3点，想到此时露露还在工作，不禁留下了心疼的泪水。
    结果，
    第二天睡醒被某狗仔爆料露露和屁屁昨天晚上在一起。
    你露出恍然大悟的神情，“怪不得昨天屁屁这么菜，可能是露露打的。”
    
    [完]
    ''')      
    
def elevenClock():
        print('''
        此时，来到北京时间的11点，亮亮还在和粉丝唠嗑，
        而露露还在做头发没有回家。
        粉丝问亮亮，露露呢?
        亮亮幸福地回答：做头发去了。
        ''')
        print('''
        露露什么时候做完头发？''')
        
        answer2 = input('''
        A：12点前不回家就打电话问问。
        B：随便做到几点钟，露露是个好女孩。
        你的回答(A/B): 
        ''')
        if answer2.lower() == 'a':
            twelfClock()
        elif answer2.lower() == 'b':
            greenHat()
        else:
            print('''
            回答无效，请输入A或者B。''')
            elevenClock()
                    
def twelfClock():
    print('''
    此时时针指向12点，露露还未回家，露露去哪儿了？
    ''')
    answer3 = input('''
    A：不管了，我先睡吧。
    B：好捉急，我要给露露打电话。
    ''')
    if answer3.lower() == 'a':
        greenHat()
    elif answer3.lower() == 'b':
        callLulu()
    else:
        print('''
        回答无效，请输入A或者B。''')
        elevenClock()

    
def callLulu():
    print('''
    给露露打电话，露露说和苏苏一起，晚上不回家了。''')
    answer4 = input('''
    A：你高兴得说：“好的，宝宝，我先睡了。爱你。”
    B：你有点生气，“你在哪儿呢？我来接你。”
    你的回答(A/B): 
    ''')
    if answer4.lower() == 'a':
        greenHat()
    elif answer4.lower() == 'b':
        pickUpLulu()
    else:
        print('''
        回答无效，请输入A或者B。''')
        elevenClock()
        
def pickUpLulu():
    print('''
    露露说：“我和苏苏要商量新剧本，可能会很晚，真的回不来了。”
    ''')
    answer5 = input('''
    A：爱她当然就要选择相信她啊，乖乖睡觉。
    B：嘻嘻，好吧。那我只好也去play了。
    你的回答(A/B): 
    ''')
    if answer5.lower() == 'a':
        greenHat()
    elif answer5.lower() == 'b':
        playHat()
    else:
        print('''
        回答无效，请输入A或者B。''')
        pickUpLulu()
          
if __name__ == '__main__':
    hairStyle()
    