# 暂停一秒输出，并格式化当前时间。 
import time as t

def FunTest():
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
