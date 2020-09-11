import turtle

turtle.title("My Turtle Anim")
turtle.setup(425,425, 0,0)

turtle.pencolor("#FF0000")
turtle.fillcolor("#FF0000")
turtle.begin_fill()
turtle.forward(70)
for i in range(4):
  turtle.right(72)
  turtle.forward(70)
turtle.end_fill()

turtle.penup() #stop drawing
turtle.goto(70, 90)
turtle.pendown() #means start drawing again

turtle.pencolor("#0000FF")
turtle.forward(1)
for i in range(360):
  turtle.right(1)
  turtle.forward(1)

turtle.exitonclick()
