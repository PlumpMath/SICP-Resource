# -*- coding: utf-8 -*-

"""
PROGRAM find_sqrt_v2

this is program is version2 of find_sqrt which is a realization of sec.1.1.7 of SICP using recursion.
It modified the part of 'goodenough' to make it suitable for small and large #.

author: YUE Shaosheng
Last Modify: 20160710
"""


def find_sqrt(x0, a):
    if goodenough(x0, a):
        print x0  # 为什么不能写成return...
    else:
        find_sqrt(improved_x0(x0, a), a)


def goodenough(x0, a):
    return abs(improved_x0 - x0) / x0 * 1. < 0.0001


def improved_x0(x0, a):
    return (x0 + a / x0) / 2.
