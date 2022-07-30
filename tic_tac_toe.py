# Importing required modules
import pygame as pg
from pygame.locals import *
import time
import sys


# Initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# Tic-tac-toe 3x3 board
board = [[None]*3, [None]*3, [None]*3]

# Initializing pygame window
pg.init()
fps = 30
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic-Tac-Toe")

# Loading images
opening = pg.image.load("tic tac opening.png")
x_img = pg.image.load("X.png")
o_img = pg.image.load("O.png")
# resizing images
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (width, height + 100))


def game_opening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (2*(width/3), 0), (2*(width/3), height), 7)
    # Drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, 2*(height/3)), (width, 2*(height/3)), 7)
    draw_status()


def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s turn"
    if winner == "x":
        message = "X " + "Won!"
    if winner == "o":
        message = "O " + "Won!"
    if draw:
        message = "Game draw!"
    font = pg.font.Font(None, 30)
    text = font.render(message, True, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


def win_check():
    global board, draw, winner

    # check for winning in row
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6), 4)
            break

    # check for winning in col
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break

    # check for diagonal winner
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4) 

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if all([all(row) for row in board]) and winner is None:
        draw = True
    draw_status()


def draw_xo(row, col):
    global board, XO

    if row == 1:
        pos_x = 30
    if row == 2:
        pos_x = width/3 + 30
    if row == 3:
        pos_x = 2*(width/3) + 30

    if col == 1:
        pos_y = 30
    if col == 2:
        pos_y = height / 3 + 30
    if col == 3:
        pos_y = 2 * (height / 3) + 30
    board[row-1][col-1] = XO
    if XO == 'x':
        screen.blit(x_img, (pos_y, pos_x))
        XO = 'o'
    else:
        screen.blit(o_img, (pos_y, pos_x))
        XO = 'x'
        pg.display.update()


def user_click():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get column of mouse click (1-3)
    if x < width/3:
        col = 1
    elif x < 2*(width/3):
        col = 2
    elif x < width:
        col = 3
    else:
        col = None
    # get row of mouse click (1-3)
    if y < height/3:
        row = 1
    elif y < 2*(height/3):
        row = 2
    elif y < height:
        row = 3
    else:
        row = None
    if row and col and board[row-1][col-1] is None:
        global XO
        # draw the x or o on screen
        draw_xo(row, col)
        win_check()


def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]


game_opening()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    pg.display.update()
    clock.tick(fps)
