import pygame
from pygame.examples.headless_no_windows_needed import screen

import consets

def create_image(img, size):
    #img = כתובת URL
    # size = טאפל של מיקום התמונה
    image = pygame.image.load(img)
    sized_image = pygame.transform.scale(image, size)



def drow_image(img):
    pass

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

def drow_game():
    screen.fill(consets.BACKGROUNDE_COLOR)
    drow_image("images/grass.png", )