# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def FunTest(n):
    while n not in [1] : # 循环保证递归
        for index in xrange(2, n + 1) :
            if n % index == 0:
                n /= index # n 等于 n/index
                if n == 1: 
                    print(index)
                else : # index 一定是素数
                    print('{} *'.format(index),)
                break

if __name__ == "__main__":
    FunTest(90)