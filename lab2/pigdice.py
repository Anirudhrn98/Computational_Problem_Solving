"""

file: pigdice.py
description: uses turtle and canvas to design the game 'Pig'
language: python3
author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu

"""

import score
import tkinter as tk
from random import randint
import turtle
import math

kpr = score.Keeper()

def draw_outline():
    """
    function to draw the outline of the die.
    start from the (0,0) position and move forward the length of the 50
    and change orienation by 90 degrees and continue to draw a square.

    :return: None
    """
    tt.down()
    tt.fd(50)
    tt.left(90)
    tt.fd(50)
    tt.left(90)
    tt.fd(50)
    tt.left(90)
    tt.fd(50)
    tt.left(90)
    tt.up()

def draw_center_dot():
    """
    function to draw the centre dot of the die
    use draw_outline function to draw the die and then move half the 50
    of the die and change angle by 90 to reach centre and draw the dot and
    then return to the (0,0) position.

    :return: None
    """
    tt.pen()
    tt.forward(50 / 2)
    tt.left(90)
    tt.forward(50 / 2)
    tt.dot(4, "black")
    tt.back(50 / 2)
    tt.right(90)
    tt.back(50 / 2)

def draw_two_dots():
    """
    function to draw a die with 2 dots.
    use draw_outline function to draw the die and then change orienation to
    the diagonal of the square and move up and draw 2 dots and return to the
    (0,0) position

    :return: None
    """

    tt.left(45)
    tt.fd((50*math.sqrt(2))/4)
    tt.down()
    tt.dot(4,"Black")
    tt.up()
    tt.fd((50*math.sqrt(2))/2)
    tt.down()
    tt.dot(4,"Black")
    tt.up()
    tt.back((3*50*math.sqrt(2))/4)
    tt.right(45)

def draw_four_dots():
    """
    function to draw to a die with 4 dots.
    Use the function used to draw the 1st two dots then change the orientation
    and draw the other two dots.

    :return: None
    """

    draw_two_dots()
    tt.forward(50)
    tt.left(90)
    draw_two_dots()
    tt.forward(50)
    tt.left(90)
    tt.forward(50)
    tt.left(90)
    tt.forward(50)
    tt.left(90)

def draw_six_dots():
    """
    function to draw to a die with 4 dots.
    Use the function used to draw the 1st two dots then change the orientation
    and draw the other two dots.

    :return: None
    """
    tt.up()
    tt.forward(50 / 3)
    tt.left(90)
    tt.forward(50 / 4)
    tt.down()
    tt.dot(4 , "black")
    tt.up()
    tt.forward(50 / 4)
    tt.down()
    tt.dot(4, "black")
    tt.up()
    tt.forward(50 / 4)
    tt.down()
    tt.dot(4, "black")
    tt.up()
    tt.right(90)
    tt.forward(50 / 3)
    tt.down()
    tt.dot(4, "black")
    tt.up()
    tt.right(90)
    tt.forward(50 / 4)
    tt.down()
    tt.dot(4, "black")
    tt.up()
    tt.forward(50 / 4)
    tt.down()
    tt.dot(4, "black")
    tt.up()
    tt.forward(50 / 4)
    tt.right(90)
    tt.forward(2*50 / 3)
    tt.left(180)

def draw_die(pips):
    """
    function to print die with dots ranging from 1-6.
    use the centre_dot, two_dot and four_dot functions to draw die with dots
    from 1-6. use centre_dot and two_dot to draw die with three dots and five
    dots. use the six_dot to draw die with 6 dots.

    :param pips: decides the number of dots which with the die has to be drawn.
    :return: None
    """

    assert isinstance(pips, int), "Illegal #pips: " + str( pips )
    draw_outline()


    if (pips == 1):
        draw_center_dot()

    elif (pips == 2):
        draw_two_dots()

    elif (pips == 3):
        draw_two_dots()
        draw_center_dot()

    elif (pips == 4):
        draw_four_dots()

    elif (pips == 5):
        draw_center_dot()
        draw_four_dots()

    elif (pips == 6):
        draw_six_dots()

    else:
        print("Invalid Value")


def roll_dice():
    """
    function to roll the die using randint and check if the score of
    the player has reached 50 and then terminate the game or if the
    die rolls 1 then terminate the turn and store score of that turn and the
    turn continues with the next player.

    :param: None
    :return: None
    """

    # Reset die elements
    tt.reset()
    tt.goto(-20, 0)

    #Generate random integer
    i = randint(1, 6)

    # Roll the dice
    draw_die(i)

    # Check if score is less then fifty
    if(kpr.score[0] < 50 and kpr.score[1] < 50 and i!=1):
        kpr.add_points(i)
        display_turn_score()

    # reset turn score and switch player when dice shows 1
    elif(i==1):
        kpr.points=0
        hold()

    # Exit the game when score reaches 50 for any player
    elif (kpr.score[0] >= 50 or kpr.score[1] >= 50):
        game_end(kpr.score[0] >= 50)
        turtle.exitonclick()

def game_end(winner):
    '''
    function to check which player has won the game and display the result
    accordingly.
    :param winner: true/false depending on which player wins the game.
    :return:
    '''

    if(winner==True):
        tt_head.ht()
        tt_head.up()
        tt_head.goto(-100, -100)
        tt_head.color("Green")
        tt_head.write(" Game Ended : Player 1 won ", font=("Arial", 12, "normal"))

    if (winner == False):
        tt_head.ht()
        tt_head.up()
        tt_head.goto(-100, -100)
        tt_head.color("Green")
        tt_head.write(" Game Ended : Player 2 won ", font=("Arial", 12, "normal"))




def hold():
    '''
    function to switch the player turn if the button is clicked and reset
    the turn score and the die.
    :param : None
    :return: None
    '''

    # Initiates the player switch
    kpr.switch_player()

    # Refreshes the player score
    display_player_score()
    tt.reset()
    tt.goto(-20,0)
    draw_outline()
    display_turn_score()

def mouse_click(x,y):
    '''
    function to read the input of mouse click from the user to decide whether
    to roll die for the again or hold and proceed with the turn of the
    next player.
    :param x: used to determine where the mouse click is on x-axis
    :param y: used to determine where the mouse click is on y-axis
    :return:
    '''

    game_header()

    # checks if cursor is in the range of dice button
    if(x>=-20 and x<=30 and y<=50 and y>=0):
        roll_dice()

    # checks if cursor is in the range of hold button
    if(x>=-20 and x<=30 and y<=-20 and y>=-40):
        hold()


def display_turn_score():
    """
    function to display the score that is achieved the current turn.
    It is displayed above the die and between the score of both the player.

    :param None
    :return None
    """

    # Move turtle and print the turn score after die roll
    tt.up()
    tt.ht()
    tt.goto(36,67)
    tt.down()
    tt.write(str(kpr.points),font=("Arial", 9, "normal"))
    tt.up()
    tt.goto(-20,0)
    tt.st()


def display_player_score():
    """
    function to store the score of the respective players after each turn.
    when player 1 clicks hold after his/her turn, score of player 1 will be
    stored and respectively for player 2.

    This function is triggered at the end of each player's turn

    :param None
    :return None
    """

    # Functionality for player 1
    if(kpr.player==1):

        # Clear any previous drawings by the turtles
        P1_tt.clear()
        P1_st.clear()
        P2_tt.clear()

        # Change the player 1's interface to black indicating the turn is over
        P1_tt.up()
        P1_tt.ht()
        P1_tt.goto(-210, 190)
        P1_tt.down()
        P1_tt.color("black")
        P1_tt.write("Player 1 Score :",font=("Arial", 10, "bold"))

        # Printing the player 1's score after the end of turn
        P1_st.up()
        P1_st.ht()
        P1_st.goto(-105, 190)
        P1_st.down()
        P1_st.write(str(kpr.score[0]),font=("Arial", 10, "bold"))

        # Change the player 2's interface to blue indicating start of turn
        P2_tt.up()
        P2_tt.ht()
        P2_tt.goto(110, 190)
        P2_tt.down()
        P2_tt.color("Blue")
        P2_tt.write("Player 2 Score :",font=("Arial", 10, "bold"))
        P2_tt.up()

    # Functionality for player 1
    if (kpr.player == 0):

        # Clear any previous drawings by the turtles
        P2_tt.clear()
        P2_st.clear()
        P1_tt.clear()

        # Change the player 2's interface to black indicating the turn is over
        P2_tt.up()
        P2_tt.ht()
        P2_tt.goto(110, 190)
        P2_tt.down()
        P2_tt.color("black")
        P2_tt.write("Player 2 Score :",font=("Arial", 10, "bold"))

        # Printing the player 1's score after the end of turn
        P2_st.up()
        P2_st.ht()
        P2_st.goto(220, 190)
        P2_st.down()
        P2_st.write(str(kpr.score[1]),font=("Arial", 10, "bold"))

        # Change the player 2's interface to blue indicating start of turn
        P1_tt.up()
        P1_tt.ht()
        P1_tt.goto(-210, 190)
        P1_tt.down()
        P1_tt.color("Blue")
        P1_tt.write("Player 1 Score :",font=("Arial", 10, "bold"))
        P1_tt.up()


def game_header():
    """
    function to display the header of the game and it randomizes the colour
    of the header using randint function. The colour changes after each click
    of the die.

    :param None
    :return None
    """

    # Positioning the turtle to write game header
    tt_head.ht()
    tt_head.up()
    tt_head.goto(-45, 185)

    # Generate random integer to select colours
    r=randint(0,4)

    # List of colors for game header
    color_var = ("red", "yellow", "blue", "green", "orange")
    tt_head.color(color_var[r])

    # Write game header using turtle
    tt_head.write(" PiG DiCe ", font=("Arial", 15, "bold"))


def initialize_game():
    """
    function to create the GUI required for the game using 'canvas'.
    It creates the hold button, turn total display, contains dimensions
    of the elements, calls the game header to display the name of the game,
    displays the total score each player and also defines the color
    and the font of the text used.

    :param None
    :return None
    """

    # Setting screen dimensions
    screen.setup(500, 500)

    # Setting screen background color to white
    screen.bgcolor("white")

    # Getting canvas to place game elements on
    canvas = screen.getcanvas()

    # create rectangle to enclose the hold button
    canvas.create_rectangle(-20, 40, 30, 20)
    canvas.create_text(5, 30, text="Hold", width=800)



    # Create the turn total text on the canvas
    tt_head.ht()
    tt_head.up()
    tt_head.goto(-35,67)
    tt_head.write(" Turn Total :", font=("Arial", 9, "normal"))


    # Creating outline of the die button
    tt.goto(-20, 0)
    tt.ht()
    draw_outline()

    ## UI elements
    canvas.create_rectangle(-250, -150,-70, -300)
    canvas.create_rectangle(70, -150, 250, -300)

    ## Function to create and refresh the game header color
    game_header()

    ## Initializing Player UI elements for first time use
    P1_tt.up()
    P1_tt.ht()
    P1_tt.goto(-210, 190)
    P1_tt.down()
    P1_tt.color("blue")
    P1_tt.write("Player 1 Score : " + "0",font=("Arial", 10 , "bold"))

    P2_tt.up()
    P2_tt.ht()
    P2_tt.goto(110, 190)
    P2_tt.down()
    P2_tt.write("Player 2 Score : " + "0",font=("Arial", 10, "bold"))



if __name__ == "__main__":
    """
    Main function to create and initiate game
    :param None
    :return None
    """

    # Turn off turtle animation and delay
    turtle.tracer(0, 0)

    # turtle used to update highlight player 1
    P1_tt = turtle.Turtle(visible=False)

    # turtle used to update update player 1 score
    P1_st = turtle.Turtle(visible=False)

    # turtle used to update highlight player 2
    P2_tt = turtle.Turtle(visible=False)

    # turtle used to update update player 2 score
    P2_st = turtle.Turtle(visible=False)

    # turtle used create game header
    tt_head = turtle.Turtle(visible=False)

    # turtle used implement die functionality
    tt = turtle.Turtle(visible=False)

    # Create screen to put on elements of the game
    screen = turtle.Screen()

    # Function initializes UI elements of the game
    initialize_game()

    # Enables button functionality to roll the die
    screen.onclick(mouse_click, btn=1, add=None)

    turtle.done()



