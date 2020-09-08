# 输出 9*9 乘法口诀表。

def FunTest():
    for i in range(1,10):
        print
        for j in range(1,i + 1):
            print("%d*%d=%d" % (i, j, i*j))

if __name__ == "__main__":
    FunTest()