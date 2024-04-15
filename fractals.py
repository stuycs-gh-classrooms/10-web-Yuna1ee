import turtle
window = turtle.Screen()

def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(size)
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
raphael.goto(-295, -290)
raphael.pd()
koch_curve(raphael, 3, 100)

def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def sierpinski(t, depth, size, scale_factor=1):
    if depth == 1:
        triangle(t, size)
    else:
        sierpinski(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2)
        t.bk(size/2)
        t.lt(60)
        t.fd(size/2)
        t.rt(60)
        sierpinski(t, depth-1, size/2)
        t.rt(120)
        t.fd(size/2)
        t.lt(120)
        
raphael.pu()
raphael.goto(-295, -290)
raphael.pd()
sierpinski(raphael, 5, 200)

window.exitonclick()