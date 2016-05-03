__author__ = 'Vigo'

# 位图
# range() return object of range, not list
a = list(range(1000))

shift = 5

max_length = 0x1f


def set_bit(i):
    a[i >> shift] = (a[i >> shift] | (1 << (i & max_length)))


def clear_bit(i):
    a[i >> shift] &= ~(1 << (i & max_length))


def check_bit(i):
    res = a[i >> shift] & (1 << (i & max_length))
    if res == 0:
        print(i, " is not in array")
    else:
        print(i, " is in array")


for n in a:
    set_bit(n)

check_bit(54)
check_bit(10001)


