 #turtle for draw circle
import turtle
t = turtle.Turtle()
bd = turtle.title("Flag Of Bangladesh")
#t.hideturtle()
t.color("green")#turtle color
t.begin_fill()
t.fillcolor("green")#bg color
t.speed(1)
t.forward(300)
t.right(-90)
t.forward(200)
t.right(-90)
t.forward(300)
t.right(-90)
t.forward(200)
t.end_fill()
t.begin_fill()
t.fillcolor("green")
t.right(-90)
t.forward(185)
t.right(-90)
t.forward(100)
t.end_fill()

for i in range(2):
    t.begin_fill()
    t.fillcolor("red")
    t.circle(50)
    t.end_fill()

t.color("green")
t.hideturtle()
t.right(180)
t.forward(200)
t.write('BANGLADESH', True, align="center",font= 18) 
#text = turtle.textinput("asa","5")



