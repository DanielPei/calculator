# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 2019/12/11 23:09

from calculator_demo.op import hello_world, CalculatorUtil


def test_hello_world():
    assert hello_world() == "Hello, World!"
    assert hello_world("Daniel") == "Hello, Daniel!"

def test_add():
    assert CalculatorUtil.add_num(1,1) == 2

if __name__ == '__main__':
    pass