import turtle

turtle.shape('turtle')
turtle.speed(1)
turtle.pencolor('red')

def draw_square(side):
    counter = 0
    while counter < 4:
        turtle.fd(side)
        turtle.left(90)
        counter += 1

draw_square(250)
turtle.done()
