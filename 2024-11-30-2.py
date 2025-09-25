def search(n):
    dictionary = {
        "广东": ["广州", "深圳", "惠州", "珠海"],
        "四川": ["成都", "内江", "乐山"],
        "贵州": ["贵阳", "六盘水", "遵义"],
    }
    for i, j in dictionary.items():
        if n == i:
            print(i, end=": ")
            for m in j:
                print(m, end=" ")
            return
        elif n in j:
            print(n, "在", i, "省")
            return
    print("没有找到")

search(input("请输入省份或城市: ").replace(" ", ""))
