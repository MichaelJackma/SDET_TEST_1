# -*- coding: utf-8 -*-
'''
@Date   : 2021/9/16 23:50
@Author : Michael_Jackma
@Email  : Michael_Jackma@163.com
@File   : calc.py
'''


# 被测模块
# 实现计算器计算

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return '被除数不能为0'
        else:
            return a / b
