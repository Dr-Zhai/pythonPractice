print("计算字符串中大写字母和小写字母的个数\n")


def letter_cal(s: str = "Hello! Welcome to Python!"):
    a = 0
    b = 0
    for ch in s:
        if ch.isupper():
            a += 1
        elif ch.islower():
            b += 1
    return a, b


d = letter_cal(input("请输入字符串: "))
print(d, type(d), "\n")
print(f"大写字母个数为: {d[0]}")
print(f"小写字母个数为: {d[1]}", "\n")


def ctRound(r):
    c = r * 2 * 3.1415926
    s = r ** 2 * 3.1415926
    return c, s


d = ctRound(eval(input("请输入圆的半径: ")))
print("圆的周长为: " + "%.1f" % d[0])
print("圆的面积为: " + "%.1f" % d[1])
