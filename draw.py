import turtle
def drawSquare():
    sq = turtle.Turtle()
    window = turtle._getscreen()
    window.bgcolor("red")
    sq.shape('turtle')
    sq.speed(2)
    sq.color('yellow')
    for i in range(40):
        for i in range(4):
            sq.forward(100)
            sq.right(90)
        sq.right(10)

    window.exitonclick()

drawSquare()
