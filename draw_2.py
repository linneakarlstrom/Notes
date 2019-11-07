import turtle
import random

yay = turtle.Turtle()

turtle.bgcolor("black")

color = ("pink", "turquoise", "light green")

for x in range(137):
    colorchoice = random.choice(color)
    yay.color(colorchoice)
    yay.width(x/100 + 1)
    yay.forward(x)
    yay.left(67)

turtle.done()

# vill du ha random färger skriv colorchoice = random.choice(color) sedan namnet på filen .color
# men först måste du skriva color = ("här skriver du vilka färger du vill ha")