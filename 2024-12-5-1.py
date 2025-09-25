# print("计算1!+2!+3!+...+n!的值\n")
#
#
# def fac(k):
#     i = 2
#     t = 1
#     while i <= k:
#         t *= i
#         i += 1
#     return t
#
#
# def sum_1(m):
#     s = 0
#     i = 1
#     while i <= m:
#         s += fac(i)
#         i += 1
#     return s
#
#
# n = eval(input("输入阶乘数为: "))
# print("1!+2!+3!+...+", n, "! =", sum_1(n))

print("计算n的阶乘\n")


def func(count):
    if count == 1:
        result = 1
    else:
        result = func(count - 1) * count
    return result


number = eval(input("请输入一个正整数: "))
print(number, "的阶乘为:", "{:.1e}".format(func(number)))
