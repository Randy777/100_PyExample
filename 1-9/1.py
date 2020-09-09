# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def testFun():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if((i!=k) & (i!=j) & (j!=k)):
                    print(i,j,k)


if __name__ == "__main__":
    print("Hello World")
    testFun()
