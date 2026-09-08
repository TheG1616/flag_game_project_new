from importlib.metadata.diagnose import run

import pygame
import consets
import screen
import game_field

run = True


def main():
    pygame.init()
    pygame.display.set_caption("The_Flag_Game")

    game_field.generate_random_dungeon()
    while run:


        handle_user_events()

        screen.drow_game()





def handle_user_events():
    global run

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.K_KP_ENTER:
            pass


if __name__ == '__main__':
    main()