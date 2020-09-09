# 判断101-200之间有多少个素数，并输出所有素数。
from sys import stdout
from math import sqrt

def FunTest():
    # l = []
    h = 0
    for i in range(101,201):
        leap = 1
        k = int(sqrt(i + 1))
        for j in range(2,k + 1):
            if i % j == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % i)
            # h += 1
            h += 1
    print("The total is : ", h)

if __name__ == "__main__":
    FunTest()        