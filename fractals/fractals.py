import turtle
import random
window = turtle.Screen()

def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(random.randrange(size))
    else:
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        t.rt(120)
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        

raphael = turtle.Turtle()
raphael.pu()
raphael.goto(-450, 0)
raphael.pd()
koch_curve(raphael, 4, 50)
window.exitonclick()