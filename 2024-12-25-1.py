import string

speach = []
count = 0
sentence = open("dream.txt", "r", encoding="utf-8")

for words in sentence:
    temp = words.split()
    speach.extend(temp)
count = len(speach)
print(speach)
print("文件长度为: %d" % count)

purSpeach = []
for word in speach:
    newWord = ""
    for char in word:
        if char not in string.punctuation:  # 用于去除标点符号
            newWord += char
    purSpeach.append(newWord)
count = len(purSpeach)
print(purSpeach)
print("文件长度为: %d" % count)

unique = []
for word in purSpeach:
    word = word.lower()
    if word not in unique:
        unique.append(word)

for word in unique:
    count += 1
    print(word, end=" ")
print("\n不重复的单词个数为:", len(unique))
