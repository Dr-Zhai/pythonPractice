tempStr = input("请输入带有符号的温度值: ")
cc = ('c', 'C')
fc = ('f', 'F')
if tempStr[-1] in fc:
    c = (eval(tempStr[:-1]) - 32) / 1.8
    print("转换为摄氏度后是%.1f°C" % c)
elif tempStr[-1] in cc:
    f = 1.8 * eval(tempStr[:-1]) + 32
    print("转换为华氏度后是%.1f°F" % f)
else:
    print("输入格式错误")

# str[]使用示例
exStr = "abcdef"
print(exStr[2:])  # cdef
print(exStr[:2])  # ab
print(exStr[-2:])  # abcd
print(exStr[:-2])  # ef
print(exStr[1:3])  # 1 ~ 3-1    bc
# eval函数使用示例
print(eval("1+2"))
print(eval("[*'123']"))  # 解包操作
a = 2
print(eval("a"))  # 引入变量
print(eval("a*4"))  # 引用变量并计算
print(eval("{'b': c}", {"c": 10}))  # 指定变量的值
print(eval("[i for i in range(3)]"))  # 列表推导公式
