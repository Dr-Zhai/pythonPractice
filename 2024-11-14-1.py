def formatInt(n):
    print("|%d|" % n)
    print("|%4d|" % n)
    print("|%-4d|" % n)
    print("|%04d|" % n)
    print("|%-04d|" % n)


def formatFloat(n):
    print("|%f|" % n)
    print("|%8.1f|" % n)
    print("|%8.2f|" % n)
    print("|%08.3f|" % n)
    print("|%-08.2f|" % n)
    print("|%-8.1f|" % n)
    print("|%-8.0f|" % n)
    print("|%g|" % n)


def formatStr(s):
    print("|%s|" % s)
    print("|%8s|" % s)
    print("|%-8s|" % s)


i = 12
formatInt(i)
i = 12345
formatInt(i)
print("|{0:*^3,}|".format(i))
print("|{0:*^8,}|".format(i))
print("|{0:^08,}|".format(i))

i = 12.57432
formatFloat(i)
print("|{0:*^12,.3g}|".format(i))

i = "abcd"
formatStr(i)

i = "I love Python!"
print("|{0:*^10.5}|".format(i))

print("你好，{1}，你这个月的工资是{0}元！{0}: {1}".format(10000, "张三"))
