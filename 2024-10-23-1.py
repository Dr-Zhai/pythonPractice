import random


class1 = int(random.random() * 2) + 3
classmate = int(random.random() * 40) + 1
print(f"请大数据240{class1}班{classmate}号同学回答问题")

"""
num1 = random.randint(1, 50)  # int(random.random() * 50) + 1
num2 = random.randint(1, 50)  # int(random.random() * 50) + 1

correct_answer = num1 + num2
user_answer = int(input(f"{num1} + {num2} = "))

if user_answer == correct_answer:
    print("恭喜你，回答正确！")
else:
    print("很遗憾，回答错误，正确答案是:", correct_answer)
"""

# random.seed(10)
score = 0
for i in range(10):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    user_answer = int(input(f"{num1} + {num2} = "))
    if user_answer == correct_answer:
        print("恭喜你，回答正确！")
        score += 10
    else:
        print("很遗憾，回答错误，正确答案是:", correct_answer)
print("你的考试分数为:", score)
