import sys
import random

__author__ = 'Vigo'

# 输入两个整数m和n，其中m<n。输出是0~n-1范围内的m个随机整数的有序列表，不允许重复，要求每个选择出现的概率相等。

# generate a big random number


def big_rand():
    return random.randint(0, sys.maxsize)


def gen_rand(m, n):
    for i in range(n):
        if (big_rand() % (n - i)) < m:
            print(i)
            m -= 1
        if m == 0:
            print("have generated enough numbers")
            break


gen_rand(3, 100)
