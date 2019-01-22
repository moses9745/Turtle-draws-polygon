#Created by D. Morris on January 22, 2019 
#Purpose: CS152DLSP2019 Introduction to Python Programming assignment question 6
#Task: Creat a turtle that will draw a polygon according to user input. 
#      Ask the user how many sides?, what color?, and how big?

#user input:
sides = int(input('How many sides (3,4,5,6,8) ?'))
length = int(input('What is the length?'))
color = input('What is the color of the turtle?')
fill_color = input('What is the fill color?')

#setting up the turtle:
import turtle
wn = turtle.Screen()
wn.bgcolor('black')
dave = turtle.Turtle()
dave.shape('turtle')
dave.color(color)
dave.fillcolor(fill_color)
dave.speed(3)

#defining shapes:
def draw_polygon(sides,length):
    dave.pendown()
    dave.begin_fill()
    for steps in range(sides):
        dave.forward(length)
        dave.right(360/sides)
    dave.end_fill()
    
#call function here so turtle draws user's input.
draw_polygon(sides,length)    

wn.exitonclick()