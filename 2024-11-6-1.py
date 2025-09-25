import turtle

flag_width = 960
flag_height = 640
turtle.setup(flag_width, flag_height)  # 设置画布宽高
turtle.shape("turtle")  # 设置画笔为海龟形状
turtle.bgcolor("red")  # 设置背景颜色
turtle.color("yellow")  # 设置画笔颜色
turtle.speed(3)  # 设置绘画速度
# params列表保存了5颗星的绘制坐标和边长及角度
params = [
    (-416, 192, 0, 192),
    (-192, 276, -22.5, 64),
    (-120, 220, -45, 64),
    (-132, 108, 0, 64),
    (-192, 54, -22.5, 64)
]
# 使用一个循环绘制5颗星
for param in params:
    # 读取绘制参数
    drawX, drawY, drawA, drawL = param
    turtle.up()  # 抬起画笔，移动时不画线
    turtle.setheading(drawA)  # 设置画笔朝向
    turtle.goto(drawX, drawY)  # 移动画笔
    turtle.down()  # 放下画笔，移动时会画线
    turtle.begin_fill()  # 填充星星形状的话需要先调用begin_fill函数
    # 绘制星星的5条边
    for _ in range(5):
        turtle.forward(drawL / 3)  # 画笔向前移动
        turtle.left(72)  # 画笔逆时针旋转
        turtle.forward(drawL / 3)  # 画笔向前移动
        turtle.right(144)  # 画笔顺时针旋转

    turtle.end_fill()  # 填充已绘制的形状

turtle.hideturtle()  # 隐藏画笔
turtle.done()
