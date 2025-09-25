import random

print("石头剪刀布游戏开始")
options = {1: "石头", 2: "剪刀", 3: "布"}
print(options)

while True:
    player = int(input("请输入你的选择: "))
    if player not in options:
        print("无效的选择，请重新输入")
        continue

    computer = random.randint(1, 3)

    print(f"\n你的选择是: {options[player]}")
    print(f"电脑的选择是: {options[computer]}")

    if player == computer:
        print("平局！")
    elif player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
        print("你赢了！")
    else:
        print("你输了！")

    print("\n是否再来一局？ [Y]")
    play_again = input("请输入: ")
    if play_again.strip().lower() == "y":
        print("\n")
        continue
    else:
        print("游戏结束！")
        break
