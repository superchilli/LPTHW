# -*- coding: utf-8 -*-
# 0001：做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）

import random

def generate_coupon(num, length):
    code = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    couponList = []
    for i in range(num):
        coupon = ''
        for j in range(length):
            coupon += random.choice(code)
        couponList.append(coupon)
    return couponList

