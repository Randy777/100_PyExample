# 暂停一秒输出，并格式化当前时间。 
import time

def FunTest():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(5)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


if __name__ == "__main__":
    FunTest()