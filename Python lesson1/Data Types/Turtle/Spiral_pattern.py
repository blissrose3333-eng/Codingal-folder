import turtle
square=turtle.Screen()
square.bgcolor("light blue")
square.title("Turtle")
pen=turtle.Turtle()

size=0
while True:
    for i in range(4):
        pen.fd(size+1)
        pen.left(90)
        size = size - 5