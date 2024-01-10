"""

file: sunstar.py
description: uses turtle to design the sunstar pattern with given user inputs.
language: python3
author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu

"""

import math
import turtle

def draw_side(n, level, dev):
    """
    Function to draw the side of the polygon required. If the level of polygon
    required is less than or equal to "1" it will draw a straight line
    depending on the number of sides.

    :param n: length of the initial side of the polygon
    :param level: number of levels of the required polygon
    :param dev: the deflection angle of each level of the polygon
    :return: length of the total polygon drawn
    """
    if(level==0 or level==1):
        turtle.fd(n)
        return(n)

    else:
        a=draw_side(n / 4, 1,dev)
        turtle.left(dev)
        b=draw_side(n / (4 * math.cos(math.radians(dev))), level - 1,dev)
        turtle.right(2 * dev)
        c=draw_side(n / (4 * math.cos(math.radians(dev))), level - 1,dev)
        turtle.left(dev)
        d=draw_side(n / 4, 1,dev)
        return(a+b+c+d)

def draw_star(sides, n, level, dev):
    """
    Draws the star for the given user input values using recursion and the
    draw_side function. Calculates centre angle of the polygon depending
    on the number of sides.Sum which holds the total length of star is
    initialized to zero and it is incremented
    after each level is drawn.

    :param sides: number of sides in the required polygon
    :param n: length of the initial side of the polygon
    :param level: number of levels of the required polygon
    :param dev: the deflection angle of each level of the polygon
    :return: total length of the polygon drawn.
    """

    sum=0
    center_angle=360/sides
    while(sides>0):
        sum+=draw_side(n, level, dev)
        turtle.right(center_angle)
        sides=sides-1
    return(sum)

def input_value_check():
    """
    This function that takes all the inputs from the user and checks
    if it is the correct data type and send a error if it the wrong
    data type and ask for the input again.

    :return:
    """

    while True:
        n=input()
        try:
            return (int(n))
        except ValueError:
            print("Value must be a Integer. You entered a ", format(type(n)))
            print("Please enter again : ",end=" ")
            continue
        else:
            break

def main():
    """
    The main function manages all the function calls required to draw the
    figure . Also , it initializes the turtle

    :return:
    """
    # user input the number of sides in the required star.
    print("Enter the number of sides required: ",end=" ")
    numberOfSides = input_value_check()

    # user input the length of the initial side in the required star.
    print("Enter the length of the initial side: ",end=" ")
    lengthOfSide = input_value_check()

    # user input the number of levels in the required star.
    print("Enter the number of levels required: ",end=" ")
    numberOfLevels = input_value_check()

    while True:
        def_angle=input("Enter the deflection angle: ")
        try:
            # if number of levels is more than 1 then ask user for deflection angle.
            if numberOfLevels > 1:
                deflectionAngle = int(def_angle)
            else:
                deflectionAngle = 0
        except ValueError:
            print("Value must be a Integer. You entered a ", format(type(def_angle)) )
            continue
        else:
            break
    turtle.up()
    turtle.goto(-100 , 100)
    turtle.down()
    turtle.tracer(1,0)
    print("Total length is: ", draw_star(numberOfSides, lengthOfSide, numberOfLevels, deflectionAngle))

    turtle.done()

if __name__ == '__main__':
    main()