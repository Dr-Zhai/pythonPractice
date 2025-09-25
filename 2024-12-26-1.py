with open("2024-12-26-1-dream.txt", "r", encoding="utf-8") as f1, open("copy.txt", "w", encoding="utf-8") as f2:
    f2.write(f1.read())
    f1.close()
    f2.close()

print("使用tell()函数获取文件当前的读写位置\n")
with open("2024-12-26-1-dream.txt", "r", encoding="utf-8") as file:
    line = file.read(7)
    print(line)
    p = file.tell()
    print(f"当前位置: {p}")
    line = file.read(5)
    print(line)
    p = file.tell()
    print(f"当前位置: {p}")
    file.close()

with open("seek.txt", "w+") as file:
    file.write("Hello! Welcome to Python!")
    file.seek(17)
    s = file.read(6)
    print(s)
    file.close()

with open("seek.txt", "rb") as file:
    file.seek(-6, 2)
    s = file.read(5)
    print(s)
    file.close()
