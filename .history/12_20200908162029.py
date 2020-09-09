# 判断101-200之间有多少个素数，并输出所有素数。
from sys import stdout
from math import sqrt

def FunTest():
    l = []
    for i in range(101,201):
        k = int(sqrt(i + 1))
        for j in range(2,k + 1):
            if i % j == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % i)
            h += 1        