# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def FunTest(n):
    a = ""
    if n >= 90:
        a = "A"
    elif 60 <= n <= 89:
        a = "B"
    else:
        a = "C"
    return a

# if __name__ == "__mian__":
#     print("-------------")
#     print(FunTest(88))

if __name__ == "__main__":
    print("-------------")
    print(FunTest(88))
    