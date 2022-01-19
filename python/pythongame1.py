from turtle import *
from random import *
from time import *
bgcolor('light blue')
p1 = Turtle()
p2 = Turtle()
p2.shape('turtle')
p1.shape('turtle')
p1.color('green')
p2.color('black')
p1.penup()
p2.penup()
p1.goto(-300,200)
p2.goto(-300,-200)
p2.goto(310,-300)
p2.left(90)
p2.pendown()
p2.forward(550)
p2.write('Finish',font=30)
p2.penup()
p2.goto(-300,-200)
p2.right(90)
for i in range(30):
    if p1.pos() >= (310,250):
        color('light blue')
        pencolor('red')
        penup()
        backward(200)
        pendown()
        write('player one wins the game',font=('courier',24,('bold')))
        hideturtle()
        print('player one wins the game')
        break
    elif p2.pos() >= (310,-250):
        color('light blue')
        pencolor('red')
        penup()
        backward(200)
        pendown()
        write('player two wins the game', font=('courier',24,('bold')))
        hideturtle()
        print('player two wins the game')
        break
    else:
        p1.forward(randint(60,80))
        sleep(1)
        p2.forward(randint(60,80))
        sleep(1)



done()