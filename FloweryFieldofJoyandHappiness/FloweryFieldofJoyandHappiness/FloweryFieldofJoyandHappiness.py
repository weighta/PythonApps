#Alex Weight
#Andrew Petagna
#Python
#1/29/18# The Flowery Field Of Joy & Happiness

#Alex Weight
#Andrew Petagna
#Python
#1/29/18

import math as m
import turtle
import random as ran

def lawn(t):
    print("drawing lawn...")
    t.penup()
    t.color("green")
    t.setpos(-200, -100)
    t.pendown()
    t.begin_fill()
    x = 0
    while (x < 4):
        if x % 2 == 0:
            t.forward(400)
        elif x % 2 == 1:
            t.forward(100)
        t.left(90)
        x = x + 1
    t.end_fill()

def sky(t):
    print("drawing sky...")
    t.penup()
    t.setpos(-200, 0)
    t.color("darkturquoise")
    t.pendown()
    t.begin_fill()
    x = 0
    while (x < 4):
        if x % 2 == 0:
            t.forward(400)
        elif x % 2 == 1:
            t.forward(200)
        t.left(90)
        x = x + 1
    t.end_fill()
    
    #Draw Sun
    t.penup()
    t.setpos(-150, 175)
    t.pendown()
    t.color("yellow")
    t.speed(20)
    for i in range(40):
        t.circle(15)
        t.left(9)
    
def drawFlower(t, x, y, c, l, r, p):
    turtle.hideturtle()
    
    #Position
    t.penup()
    t.setpos(x, y)
    t.pendown()
    
    #Stem
    t.color("lime")
    t.left(90)
    t.forward(l)
    
    #Pollin
    t.color("yellow")
    t.right(90)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    
    #Petals
    originY = y + l + r
    t.penup()
    t.setpos(x, originY)
    t.color(c)
    #Use Trig for plotting petals!
    for i in range(p):
        t.penup()
        rad = (i * (360 / p)) * (m.pi / 180)
        t.setpos(x + (m.cos(rad) * r), (originY) + (m.sin(rad) * r))
        t.begin_fill()
        t.circle(r / 2)
        t.end_fill()
    
def main():
    colorArr = ['red', 'blue', 'purple', 'magenta', 'cyan', 'grey', 'lime', 'yellow']
    flowers = int(input("How many flowers would you like to draw?"))
    petals = int(input("How many petals should appear on a flower?"))
    
    #Plot a Grassy Lawn!
    lawn(turtle.Turtle())
    
    #Plot the Sky!
    sky(turtle.Turtle())
    
    #Plot Flowers!
    for i in range(0, flowers, 1):
        x = ran.randint(-175, 175)
        y = ran.randint(-100, 0)
        l = ran.randint(20, 35)
        r = ran.randint(4, 12)
        drawFlower(turtle.Turtle(), x, y, colorArr[ran.randint(0, 6)], l, r, petals)
        print("Flower #" + str(i + 1) + " @(x: " + str(x) + " y: " + str(y) + ")")
    print("All done! Enjoy your beautiful garden!")
    if flowers == 0:
        print("No flowers? Awe, ok.")
main()