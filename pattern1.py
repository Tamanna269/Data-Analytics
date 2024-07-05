from turtle import *
 for loop 
side = 8
for i in range (side):
         fd(120)
        lt(360/side)
mainloop()



from turtle import*
s = getscreen()
t = Turtle()
for i in range(5):
   t.fd(100)
    t.lt(72)
mainloop()

from turtle import*
speed('fast')
pencolor('red')
for i in range(100):
    fd(i*3+5)
    lt(90)
    mainloop()

rom turtle import*
fillcolor('red')
begin_fill()
for i in range(5):
        fd(100)
        lt(72)
end_fill()
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()
mainloop()

from turtle import*
pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()
    mainloop()

from turtle import*
s = Screen()
s.setup(1000,700)
colors = ['purple','blue']
pencolor('green')
pensize(5)
for i in range(6,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
    mainloop()

from turtle import*
bgcolor('black')
speed('fastest')
colors = ['red','purple','blue','green','yellow','orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x/100+1)
    forward(x)
    left(59)
    mainloop()