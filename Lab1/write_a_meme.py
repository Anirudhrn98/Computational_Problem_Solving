"""

file: write_a_meme.py
description: uses turtle to draw meme including the word 'TOM'
language: python3
author: Anirudh Narayanan, an9425g.@rit.edu

"""

#global constants for window dimensions
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


import turtle as tt
import math
tt.setup(700 ,700 )

def init():
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (-175,0), heading (east), down
    :post: pos (175,0), heading (east), up
    :return: None
    """
    tt.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                              WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    tt.up()
    tt.setheading(0)
    tt.title('TOM JERRY')
    tt.speed(6)
    tt.hideturtle()

def letter_o():
    """
       Draw aplhabet O.
       :pre: (relative) pos (0,0), heading (east), pen up
       :post: (relative) pos (30,0), heading (east), pen up
    """
    tt.down()
    tt.forward(30)
    tt.left(90)
    tt.forward(60)
    tt.left(90)
    tt.forward(30)
    tt.left(90)
    tt.forward(60)
    tt.up()
    tt.left(90)
    tt.forward(30)
    tt.forward(10)

def letter_r():
    """
        Draw aplhabet R.
        :pre: (relative) pos (0,0), heading (east), pen up
        :post: (relative) pos (30,0), heading (east), pen up
    """
    tt.down()
    tt.left(90)
    tt.forward(60)
    tt.right(90)
    tt.forward(30)
    tt.right(90)
    tt.forward(30)
    tt.right(90)
    tt.forward(30)
    tt.left(135)
    tt.forward(30 * math.sqrt(2))
    tt.left(45)
    tt.up()
    tt.forward(10)

def letter_t():
    """
        Draw aplhabet T.
        :pre: (relative) pos (0,0), heading (east), pen up
        :post: (relative) pos (30,0), heading (east), pen up
    """

    tt.up()
    tt.forward(15)
    tt.down()
    tt.left(90)
    tt.forward(60)
    tt.left(90)
    tt.forward(15)
    tt.back(30)
    tt.up()
    tt.forward(15)
    tt.left(90)
    tt.forward(60)
    tt.left(90)
    tt.forward(15)
    tt.forward(10)

def letter_m():
    """
        Draw aplhabet M.
        :pre: (relative) pos (0,0), heading (east), pen up
        :post: (relative) pos (30,0), heading (east), pen up
    """
    tt.down()
    tt.left(90)
    tt.forward(60)
    tt.right(150)
    tt.forward(30)
    tt.left(120)
    tt.forward(30)
    tt.right(150)
    tt.forward(60)
    tt.left(90)
    tt.up()
    tt.forward(10)

def letter_e():
    """
        Draw aplhabet E.
        :pre: (relative) pos (0,0), heading (east), pen up
        :post: (relative) pos (30,0), heading (east), pen up
    """
    tt.down()
    tt.left(90)
    tt.forward(60)
    tt.right(90)
    tt.forward(30)
    tt.back(30)
    tt.right(90)
    tt.forward(30)
    tt.left(90)
    tt.forward(30)
    tt.back(30)
    tt.right(90)
    tt.forward(30)
    tt.left(90)
    tt.forward(30)
    tt.up()
    tt.forward(10)

def letter_j():
    """
        Draw aplhabet J.
       :pre: (relative) pos (0,0), heading (east), pen up
        :post: (relative) pos (30,0), heading (east), pen up
        """
    tt.down()
    tt.left(90)
    tt.forward(20)
    tt.backward(20)
    tt.right(90)
    tt.forward(15)
    tt.left(90)
    tt.forward(60)
    tt.left(90)
    tt.forward(15)
    tt.back(30)
    tt.forward(15)
    tt.left(90)
    tt.forward(60)
    tt.up()
    tt.left(90)
    tt.forward(15)
    tt.forward(10)

def letter_y():
    """
        Draw aplhabet Y.
        :pre: (relative) pos (0,0), heading (east), pen up
        :post: (relative) pos (30,0), heading (east), pen up
        """
    tt.up()
    tt.left(90)
    tt.forward(60)
    tt.down()
    tt.right(154)
    tt.forward(15*math.sqrt(5))
    tt.left(138)
    tt.forward(15*math.sqrt(5))
    tt.up()
    tt.back(15*math.sqrt(5))
    tt.down()
    tt.back(15*math.sqrt(5))
    tt.right(45)
    tt.up()
    tt.forward(60)
    tt.forward(10)

def draw_tom():
    """
        Draw the word 'TOM'.
       :pre: (relative) pos (0,0), heading (east), pen up
       :post: (relative) pos (110,0), heading (east), pen up
    """
    letter_t()
    letter_o()
    letter_m()

def draw_jerry():
    """
        Draw the word 'TOM'.
      :pre: (relative) pos (0,0), heading (east), pen up
      :post: (relative) pos (110,0), heading (east), pen up
   """
    letter_j()
    letter_e()
    letter_r()
    letter_r()
    letter_y()


def main():
    """
       The main function.
       :pre: (relative) pos (0,0), heading (east), pen down
       :post: (relative) pos (175,0), heading (east), pen up
       :return: None
       """
    init()
    tt.up()
    tt.back(175)
    draw_tom()
    tt.forward(50)
    draw_jerry()
    tt.mainloop()



if __name__ == '__main__':
    main()
