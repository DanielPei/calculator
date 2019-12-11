# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 2019/12/11 22:57


def hello_world(name: str = "World"):
    """
    Say hello
    :param name: Visit name.
    """
    return "Hello, {name}!".format(name=name)


class CalculatorUtil(object):
    """
    Calculator utils class.

    Support add, minus, multiply and divide operations.
    """

    @classmethod
    def add_num(cls, num_x, num_y):
        """
        Add up two number.
        :param num_x:
        :param num_y:
        :return:
        """

        if not num_x or not num_y:
            raise ValueError("Invalid input : ( {num_x}, {num_y} )".format(num_x=num_x, num_y=num_y))

        return num_x + num_y
