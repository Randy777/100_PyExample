# 输入三个整数x,y,z，请把这三个数由小到大输出。

def FunTest(x,y,z):
    l = []
    l.append(x)
    l.append(y)
    l.append(z)
    l.sort()
    print(l)

if __name__ == "__main__":
    FunTest(12,5,7)