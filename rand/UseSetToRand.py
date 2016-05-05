import sys
import random

__author__ = 'Vigo'


# input: m and n, m < n,
# output: m random integers in the range of 0~n-1
# notice: m close to n

# Algorithm uses Set to save the random integers
# program only generate m times random number

def big_rand():
    return random.randint(0, sys.maxsize)


def generate_rand(m, n):
    rands = set()
    for i in range(n - m, n):
        rand_num = big_rand() % (i + 1)
        print(rand_num)
        if rand_num not in rands:
            rands.add(rand_num)
        else:
            rands.add(i)
    # print set
    print(rands)


generate_rand(7, 100)
