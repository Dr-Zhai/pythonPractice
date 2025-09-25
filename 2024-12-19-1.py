import calendar


def isLeap(year):
    if calendar.isleap(year):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年是平年")

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year}年是闰年")
    else:
        print(f"{year}年是平年")


while True:
    y = int(eval(input("请输入年份: ")))
    isLeap(y)
    c = input("继续吗?[Y]\n")
    if c.replace(" ", "").lower() == "y":
        continue
    break
