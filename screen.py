from time import sleep

import pygame
import random
import game_field
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
            tuple_size = (consets.CELL_SIZE * col , consets.CELL_SIZE * row)
            if matrix[row][col] == "mine":
                drow_image(create_image(consets.MINE_IMG, consets.MINE_SIZE), tuple_size)

def drow_mode_night(matrix,player_r, player_c):
    screen.fill(consets.BLACK)
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            pygame.draw.rect(screen, (0,255,0), ( j*consets.CELL_SIZE-22,  i*consets.CELL_SIZE-22,  j*consets.CELL_SIZE,  i*consets.CELL_SIZE), 1 )
    drow_mines(matrix)
    drow_soldier(consets.SOLDIER_NIGHT_IMG, player_r, player_c)
    pygame.display.flip()

def drow_soldier(soldier_img, player_r, player_c):
    drow_image(create_image(soldier_img, consets.SOLIDER_SIZE), (player_c, player_r))


def drow_all_for_space_key(board, player_r, player_c):
    drow_mode_night(board, player_r, player_c)
    sleep(2)
    screen.fill(consets.BACKGROUNDE_COLOR)
    drow_grass()


def drow_start():
    pygame.display.set_caption("The_Flag_Game")
    draw_message(consets.START_MSG, 15, consets.WHITE, (22, 22))
    drow_image(create_image(consets.FLAG_IMG, consets.FLAG_SIZE),
               (consets.WINDOW_WIDTH - consets.CELL_SIZE * consets.FLAG_ROWS,
                consets.WINDOW_HEIGHT - consets.CELL_SIZE * consets.FLAG_COLS))

def drow_game(player_r, player_c):

    drow_soldier(consets.SOLIDER_IMG, player_r, player_c)



    pygame.display.flip()