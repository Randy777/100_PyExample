# 暂停一秒输出。
import time as t

def FunTest():
    for i in range(1,15):
        print(i)
        t.sleep(1)

if __name__ == "__main__":
    FunTest()
    