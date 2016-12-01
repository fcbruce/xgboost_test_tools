#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Thu 01 Dec 2016 16:25:24
#
#

def one_to_one_map(v):
    return float(v)

def gender_map(v):
    if (v == u'男'): return 1.
    else: return 0.

def one_hot(v, k):
    if v == k: return 1.
    else: return 0.
