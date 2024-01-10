import turtle as t
import math
import random
import sys

def draw_square1(length):
    for i in range(1, 5):
        t.forward(length)
        t.left(90)

def draw_triangle1(length):
    for i in range(1,4):
        t.right(120)
        t.forward(length)

def draw_square2(length):
    draw_square1(length)
    t.forward(length/2)
    t.left(45)
    draw_square1(math.sqrt(2*(length/2)**2))
    t.right(45)

def draw_star1(length):
    draw_square1(length)
    lengthtriangle = length/math.sqrt(3)
    for i in range(1,5):
        t.forward(length/2 + lengthtriangle/2)
        draw_triangle1(lengthtriangle)
        t.forward(length/2 - lengthtriangle/2)
        t.left(90)

def draw_nested_star(length, depth):
    if depth == 0:
        return
    elif depth == 1:
        t.color('red')
        draw_star1(length)
    else:
        t.color('green')
        for i in range(1, 5):
            t.forward(length)
            t.left(90)
        lengthtriangle = length / math.sqrt(3)
        for i in range(1, 5):
            t.forward(length / 2 + lengthtriangle / 2)
            for i in range(1, 4):
                t.right(120)
                t.forward(lengthtriangle)
            t.forward(length / 2 - lengthtriangle / 2)
            t.left(90)
        t.forward(length/2)
        t.left(45)
        draw_nested_star(math.sqrt(2*(length/2)**2), depth - 1 )



def main():
    # draw_square1(100)
    # draw_triangle1(100)
    # draw_square2(100)
    # draw_star1(100)
    # draw_nested_star(100, 1)
    t.mainloop()

if __name__ == "__main__" :
    main()