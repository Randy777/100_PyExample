# 输入某年某月某日，判断这一天是这一年的第几天？
    year = 2020
    month = 6
    day = 5
def FunTest():
    months = (0,31,59,90,120,151,181,212,243,273,304,334)
    if 0 < month <= 12:
        sum = months[month] + day
    else:
        print("data error")
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print(sum)
