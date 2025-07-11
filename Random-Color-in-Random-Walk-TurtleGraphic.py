from turtle import Turtle, Screen
import random
import turtle as a

t = Turtle()
a.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b) 

directions = [0,90,180,270]
t.pensize(15)
t.speed("fast")

for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))


input("Click anywhere to exit...")
