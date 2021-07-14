import turtle
import os
from turtle import*
# Note py file and song file must be in one folder 
file = "doraemon.mp3"
os.system(file)

setup(500, 500)
#set brush
speed(10)
bgcolor("black")
shape("turtle")
colormode(255)

def drawRound(size, filled):
    pendown()
    if filled==True:
        begin_fill()
    setheading (180)
    circle(size,360)
    if filled==True:
        end_fill()

def drawRect(length, width, filled):
    setheading(0)
    pendown()
    if filled== True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled==True:
        end_fill()

def head():
 #
    color("blue","blue")
    penup()
    goto(0, 100)
    drawRound(75,True)
 #
    color("white","white")
    penup()
    goto(0, 72)
    drawRound(60 , True)

def eyes():
#left eye socket    
    color("black", "white")
    penup()
    goto(-15,80)
    drawRound(17, True)
#right eye socket
    color("black","white")
    penup()
    goto(19,80)
    drawRound(17,True)
#
    color("black","black")
    penup()
    goto(-8,70)
    drawRound(6,True)
    color("white","white")
    penup()
    goto(-8,66)
    drawRound(2,True)
#right eyeball
    color("black","black")
    penup()
    goto(12,70)
    drawRound(6,True)
    color("white","white")
    penup()
    goto(12,66)
    drawRound(2,True)

def nose():
    color("red","red")
    penup()
    goto(0,40)
    drawRound(7,True)

def mouth():
    #mouth
    color("black","black")
    penup()
    goto(-30,-20)
    pendown()
    setheading(-27)
    circle(70,55)
 #
    penup()
    goto(0,26)
    pendown()
    goto(0,-25)

def whiskers():
    color("black","black")
 # The beard in the middle on the left
    penup()
    goto(10,5)
    pendown()
    goto(-40,5)
 # The beard in the middle on the right
    penup()
    goto(10,5)
    pendown()
    goto(40,5)
 # Left upper beard
    penup()
    goto(-10,15)
    pendown()
    goto(-40,20)
 # Right upper beard
    penup()
    goto(10,15)
    pendown()
    goto(40,20)
 # Leftbeard
    penup()
    goto(-10,-5)
    pendown()
    goto(-40,-10)
 # Right beard
    penup()
    goto(10,-5)
    pendown()
    goto(40,-10)

def body():
 #Blue body
    color("blue","blue")
    penup()
    goto(-50,-40)
    drawRect(100,80,True)
 #white belly
    color("white","white")
    penup()
    goto(0,-30)
    drawRound(40,True)
 # Red ribbon
    color("red","red")
    penup()
    goto(-60,-35)
    drawRect(120,10,True)
 # White legs
    color("white","white")
    penup()
    goto(15,-127)
    pendown()
    setheading(90)
    begin_fill()
    circle(14,180)
    end_fill()

def feet():
 # Left foot
    color("black","white")
    penup()
    goto(-30,-110)
    drawRound(20,True)
 # right foot
    color("black","white")
    penup()
    goto(30,-110)
    drawRound(20,True)

def arms():
 # left arm
    color("blue","blue")
    penup()
    begin_fill()
    goto(-51,-50)
    pendown()
    goto(-51,-75)
    left(70)
    goto(-76,-85)
    left(70)
    goto(-86,-70)
    left(70)
    goto(-51,-50)
    end_fill()
 #right(arm)
    color("blue","blue")
    penup()
    begin_fill()
    goto(49,-50)
    pendown()
    goto(49,-75)
    left(70)
    goto(74,-85)
    left(70)
    goto(84,-70)
    left(70)
    goto(49,-50)
    end_fill()

def hands():
 #lefthand
    color("black","white")
    penup()
    goto(-90,-71)
    drawRound(15,True)
 #righthand
    color("black","white")
    penup()
    goto(90,-71)
    drawRound(15,True)

def bell():
 #Yellow solid circle indicates copper bell   
    color("yellow","yellow")
    penup()
    goto(0,-41)
    drawRound(8,True)
 #Black rectangle indicates pattern
    color("black","black")
    penup()
    goto(-10,-47)
    drawRect(20,4,False)
 # the black solid circle indicates the impacted metal pill
    color("black","black")
    penup()
    goto(0,-53)
    drawRound(2,True)

def package():
 # semicircle
    color("black","black")
    penup()
    goto(-25,-70)
    pendown()
    setheading(-90)
    circle(25,180)
    goto(-25,-70)
    hideturtle()

head()
eyes()
nose()
mouth()
whiskers()
body()
feet()
arms()
hands()
bell()
package()
turtle.done()
