from turtle import *

def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(200/sides)
        turtle.left(360/sides)
    turtle.end_fill()

quad = {3: "Triangle", 5 : "Pentagon", 6 : "Hexagon", 7 : "Septagon", 8 : "Octagon"}
screen = Screen()
screen.title("polygons")
screen.bgcolor("teal")
screen.setup(width = 800, height = 800)

pen = Turtle()
pen.hideturtle()
pen.speed(0)

while True:
    sides = int(input("Enter the number of sides which your polygon has: "))
    pen.clear()
    pen.color("red")
    if sides < 3:
        pen.write("Polygon must have atleast 3 sides")
    elif sides != 4:
        regular_polygon(pen, sides)
        if sides in quad:
            pen.write(quad[sides])
        else:
            pen.write(str(sides) + "-gon")
    else:
        parrallel_sides = int(input("How many parallel sides does your quadrilateral have?"))
        if parrallel_sides == 0:
            quadrilateral_name = "Unknown quadrilateral"
            pen.begin_fill()
            pen.goto(100, 100)
            pen.goto(200, 0)
            pen.goto(250, -50)
            pen.goto(300, -150)
            pen.goto(0, 0)
            pen.end_fill()
            pen.color("Red")
            pen.write(quadrilateral_name)
        elif parrallel_sides == 1:
            quadrilateral_name = "Trapezoid"
            pen.begin_fill()
            pen.forward(100)
            pen.left(120)
            pen.forward(50)
            pen.left(60)
            pen.forward(50)
            pen.left(120)
            pen.forward(50)
            pen.end_fill()
            pen.color("violet")
            pen.write(quadrilateral_name)
        elif parrallel_sides == 2:
            interior_angles = input("Are the interior angles 90 degrees? (yes/no)").lower()
            if interior_angles == "yes":
                rectangle_type = input("Are all four sides equal? (yes/no)").lower()
                if rectangle_type == "yes":
                    quadrilateral_name = "Square"
                    pen.begin_fill()
                    pen.forward(100)
                    pen.left(90)
                    pen.forward(100)
                    pen.left(90)
                    pen.forward(100)
                    pen.left(90)
                    pen.forward(100)
                    pen.end_fill()
                    pen.color("violet")
                    pen.write(quadrilateral_name)
                elif rectangle_type == "no":
                    quadrilateral_name = "Rectangle"
                    pen.begin_fill()
                    pen.forward(200)
                    pen.left(90)
                    pen.forward(100)
                    pen.left(90)
                    pen.forward(200)
                    pen.left(90)
                    pen.forward(100)
                    pen.end_fill()
                    pen.color("violet")
                    pen.write(quadrilateral_name)

            else:
                quadrilateral_name = "Parallelogram"
                pen.begin_fill()
                pen.forward(150)
                pen.left(60)
                pen.forward(100)
                pen.left(120)
                pen.forward(150)
                pen.left(60)
                pen.forward(100)
                pen.end_fill()
                pen.color("violet")
                pen.write(quadrilateral_name)

screen.exitonclick()








