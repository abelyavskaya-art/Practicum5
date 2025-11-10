
import turtle
turtle.Screen()
xc, yc, r = int(input()), int(input()), int(input())
x, y = int(input()), int(input())
turtle.up()
turtle.goto(xc, yc-r)
turtle.down()
turtle.circle(r)

turtle.up()
turtle.goto(x, y)
turtle.down()
turtle.dot(10, 'red')

turtle.up()
turtle.goto(xc - r, yc - r - 20)
turtle.down()

if ((xc - x)**2 + (yc - y)**2)**0.5 <= r:
    turtle.color('red')
    turtle.write('Точка внутри окружности')
else:
    turtle.color('red')
    turtle.write('Точка вне окружности')
turtle.hideturtle()
turtle.done()
