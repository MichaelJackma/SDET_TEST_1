# -*- coding: utf-8 -*-
'''
@Date   : 2021/9/17 00:05
@Author : Michael_Jackma
@Email  : Michael_Jackma@163.com
@File   : test_calc.py
'''

# 测试文件
import sys
import pytest

print(sys.path.append('.'))
from pythoncode.calc import Calculator


def setup_module():
    print('模块级别 setup')


def teardown_module():
    print('模块级别 teardown')


def setup_function():
    print('函数级别 setup')


def teardown_function():
    print('函数级别 teardown')


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print('类级别 setup')

    def teardown_class(self):
        print('类级别 teardown')

    def setup(self):
        print('setup')

    def teardowm(self):
        print('teardown')

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 2),
        (10, 50, 60),
        (100, 200, 300)
    ])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.sub
    def test_sub(self, a, b, result):
        assert result == self.cal.sub(a, b)

    @pytest.mark.mul
    def test_mul(self, a, b, result):
        assert result == self.cal.mul(a, b)

    @pytest.mark.div
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)
