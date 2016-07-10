# -*- coding: utf-8 -*-
"""
PROGRAM largest_two_sum

this program is the realization of ex1.3 in SICP which find the sum of the two
largest number among three numbers.

author: YUE Shaosheng
Last Modify: 20160708
"""


def largest_two_sum(x, y, z):
    if x > y:
        return x + larger(y, z)
    elif y > x:
        return y + larger(x, z)


def larger(x, y):
    if x > y:
        return x
    elif y > x:
        return y
