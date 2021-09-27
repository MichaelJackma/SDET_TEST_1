# -*- coding: utf-8 -*-
'''
@Date   : 2021/9/24 15:27
@Author : Michael_Jackma
@Email  : Michael_Jackma@163.com
@File   : conftest.py
'''

import pytest


@pytest.fixture()
def login():
    print('登录方法')
    yield ['username', 'password']
    print("teardown")
