# -*- condig: utf-8 -*-
"""
PROGRAM find_sqrt

this is program is a realization of sec.1.1.7 of SICP, which used the 
method of recursion.

author: YUE Shaosheng
Last Modify: 20160708
"""


def find_sqrt(x0, a):
    if goodenough(x0, a):
        print x0#为什么不能写成return...
    else:
        find_sqrt(improved_x0(x0, a), a)


def improved_x0(x0, a):
    return (x0 + a / x0) / 2.


def goodenough(x0, a):
    return abs(a - x0 ** 2.) < 0.0001
