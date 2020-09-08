# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# -*- coding: UTF-8 -*-
def FunTest_03(): 
    for i in range(1,85):
        if 168 % i == 0:
            j = 168 / i
            if  (i > j) & ((i + j) % 2 == 0) & ((i - j) % 2 == 0) :
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x)

