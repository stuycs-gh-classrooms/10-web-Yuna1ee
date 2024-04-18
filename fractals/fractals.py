import turtle
import random
window = turtle.Screen()

#Koch Curves
#Basic
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
    
#Width Koch
def koch_curve(t, depth, size):
    if (depth == 1):
        t.width(random.randrange(1, 5))
        t.fd(size)
    else:
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        t.rt(120)
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)

#Size Koch
def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(random.randrange(size))
    else:
        koch_curve(t, depth-1, size)
        t.lt(50)
        koch_curve(t, depth-1, size)
        t.rt(110)
        koch_curve(t, depth-1, size)
        t.lt(50)
        koch_curve(t, depth-1, size)

#Sierpinski Triangles
#Basic
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
#Width Sierpinski
def sierpinski(t, depth, size, scale_factor=1):
    t.pencolor('purple')
    if depth == 1:
        t.width(random.randrange (1, 5))
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
#Square Sierpinski
def square(t, size):
    n = 0
    while n < 4:
        t.fd(size)
        t.rt(90)
        n += 1

def sierpinski(t, depth, size, scale_factor=1):
    t.pencolor('purple')
    if depth == 1:
        square(t, size)
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
#Tree
#Basic
def tree(t, depth, size, angle):
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)
#Angle Tree
def tree(t, depth, size, angle):
    t.pencolor('purple')
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(random.randrange(0, 100))
        tree(t, depth-1, size, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)
#Flower Tree
def square(t, size):
    t.pencolor('pink')
    t.setheading(0)
    n = 0
    while n < 4:
        t.fd(size)
        t.rt(90)
        n += 1
    t.rt(90)
    t.pencolor('brown')
    
def tree(t, depth, size, angle):
    t.pencolor('brown')
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size, angle)
        square(t, size)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)
window.exitonclick()