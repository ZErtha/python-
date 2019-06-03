import turtle
turtle.setup(650,350,200,200)
turtle.penup()#画笔抬起,海龟开始飞行
turtle.fd(-250)#前进反方向250像素
turtle.pendown()#画笔放下,海龟开始爬行
turtle.pensize(25)#宽度
turtle.pencolor("purple")#颜色
turtle.seth(-40)#绝对角度
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(140)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
