import pygame
import random

import consets

screen = pygame.display.set_mode(
        (consets.WINDOW_WIDTH, consets.WINDOW_HEIGHT))

def create_image(img, size):
    #img = כתובת URL
    # size = טאפל גודל התמונה ביחס לאורך ורוחב המסך
    image = pygame.image.load(img).convert_alpha()
    small_image = pygame.transform.scale(image, size)
    return small_image



def drow_image(img, size):
    # size = טאפל של מיקום התמונה
    screen.blit(img, size)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consets.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_lose_message():
    draw_message(consets.LOSE_MESSAGE, consets.LOSE_FONT_SIZE,
                 consets.LOSE_COLOR, consets.LOSE_LOCATION)


def draw_win_message():
    draw_message(consets.WIN_MESSAGE, consets.WIN_FONT_SIZE,
                 consets.WIN_COLOR, consets.WIN_LOCATION)

def drow_grass():
    for i in range(20):
        x = random.randrange(0,consets.WINDOW_WIDTH)
        y = random.randrange(0, consets.WINDOW_HEIGHT)
        drow_image(create_image(consets.GRASS_IMG, consets.GRASS_SIZE), (x,y))


def drow_mines(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            tuple_size = (consets.CELL_SIZE * row, consets.CELL_SIZE * col)
            if matrix[row][col] == "mine":
                drow_image(create_image(consets.MINE_IMG, consets.MINE_SIZE), tuple_size)

def drow_game():
    draw_message(consets.START_MSG, 15, consets.WHITE, (22,22))



    drow_image(create_image(consets.SOLIDER_IMG, consets.SOLIDER_SIZE), (0,0))
    drow_image(create_image(consets.FLAG_IMG, consets.FLAG_SIZE), (consets.WINDOW_WIDTH - consets.CELL_SIZE * consets.FLAG_ROWS, consets.WINDOW_HEIGHT - consets.CELL_SIZE * consets.FLAG_COLS))

    drow_image(create_image(consets.MINE_IMG, consets.MINE_SIZE), (300, 300))


    pygame.display.flip()