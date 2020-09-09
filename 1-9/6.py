# 斐波那契数列。

def Fbi(n):
    if n == 1 or n == 2:
        return 1
    return Fbi(n - 1) + Fbi(n - 2)

if __name__ == "__main__":
    print(Fbi(10))