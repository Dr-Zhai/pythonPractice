months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(y):
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0


def countDays(y, m, d):
    global months
    days = d
    if isLeap(y):
        months[2] = 29
    else:
        months[2] = 28
    for n in range(1, m):
        days += months[n]
    return days


def countWeek(y, m, d):
    days = countDays(y, m, d)
    y = y - 1
    w = y + y // 4 + y // 400 - y // 100 + days
    w = w % 7
    return w


def printWeek():
    global months
    s = input("YYYY-mm-dd: ").split("-")
    if len(s) == 3:
        try:
            y = int(s[0])
            m = int(s[1])
            d = int(s[2])
            if y < 0:
                raise Exception("无效的年份")
            if m < 0 or m > 12:
                raise Exception("无效的月份")
            if isLeap(y):
                months[2] = 29
            else:
                months[2] = 28
            if d < 1 or d > months[m]:
                raise Exception("无效的日期")
            w = countWeek(y, m, d)
            week = ["日", "一", "二", "三", "四", "五", "六"]
            print(y, m, d, "星期" + week[w])
        except Exception as e:
            print(e)
    else:
        print("无效日期")


def printMonth(y, m):
    global months
    w = countWeek(y, m, 1)
    if isLeap(y):
        months[2] = 29
    else:
        months[2] = 28
    md = months[m]
    print("%-6s%-6s%-6s%-6s%-6s%-6s%-6s" % ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
    for i in range(w):
        print("%-6s" % " ", end="")
    for d in range(1, md + 1):
        print("%-6d" % d, end="")
        w = w + 1
        if w % 7 == 0:
            print()


def printCalendar():
    try:
        y = int(eval(input("请输入年份: ")))
        for m in range(1, 13):
            print()
            print(f"------------{y}年{m}月 ------------")
            printMonth(y, m)
            print()
    except Exception as e:
        print(e)


while True:
    print("1.计算某天星期几")
    print("2.打印某年的日历")
    inp = input("请选择[1,2]: ")
    if inp == "1":
        printWeek()
    elif inp == "2":
        printCalendar()
    else:
        break
