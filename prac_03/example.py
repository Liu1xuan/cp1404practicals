import turtle

# 创建一个画布
screen = turtle.Screen()
screen.bgcolor("skyblue")  # 设置背景颜色为天蓝色

# 创建一个画笔
pen = turtle.Turtle()

# 绘制太阳
pen.penup()
pen.goto(-250, 200)  # 移动画笔到太阳初始位置
pen.pendown()
pen.fillcolor("yellow")  # 设置填充颜色为黄色
pen.begin_fill()  # 开始填充
pen.circle(50)  # 绘制太阳
pen.end_fill()  # 结束填充

# 绘制草地
pen.penup()
pen.goto(-300, -150)  # 移动画笔到草地初始位置
pen.pendown()
pen.fillcolor("green")  # 设置填充颜色为绿色
pen.begin_fill()  # 开始填充
pen.forward(600)  # 绘制草地
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(600)
pen.left(90)
pen.forward(150)
pen.end_fill()  # 结束填充

# 绘制树干
pen.penup()
pen.goto(-100, -150)  # 移动画笔到树干初始位置
pen.pendown()
pen.pensize(20)  # 设置画笔大小为20
pen.pencolor("brown")  # 设置画笔颜色为棕色
pen.forward(100)  # 绘制树干

# 绘制树冠
pen.penup()
pen.goto(-200, -50)  # 移动画笔到树冠初始位置
pen.pendown()
pen.fillcolor("darkgreen")  # 设置填充颜色为深绿色
pen.begin_fill()  # 开始填充
pen.circle(100)  # 绘制树冠
pen.end_fill()  # 结束填充

# 隐藏画笔
pen.hideturtle()

# 点击画布关闭程序
screen.exitonclick()
