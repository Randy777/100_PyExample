# 暂停一秒输出，并格式化当前时间。 
import time as t

def FunTest():
    print t.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    t.sleep(5)
    print t.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
