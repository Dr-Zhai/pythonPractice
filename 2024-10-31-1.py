def op(num):
    return bin(num).replace("0b", "").zfill(8)

a = 10
b = 23

print("a的一个字节二进制表示:", op(a))
print("b的一个字节二进制表示:", op(b))
print("a & b =", op(a & b))
print("a | b =", op(a | b))
print("a ^ b =", op(a ^ b))
print("~a =", op(~a))
print("~b =", op(~b))
print("a << 2 =", op(a << 2))
print("a >> 2 =", op(a >> 2))
print("b << 2 =", op(b << 2))
print("b >> 2 =", op(b >> 2))
print("a的十进制表示:", a, "a的八进制表示:", oct(a), "a的十六进制表示:", hex(a))
print("b的十进制表示:", b, "b的八进制表示:", oct(b), "b的十六进制表示:", hex(b))
