import pygame
import consets
import screen
import game_field


def main():
    pygame.init()
    pygame.display.set_caption("The_Flag_Game")

    game_field.generate_random_dungeon()
    while True:
        screen.drow_game()

if __name__ == '__main__':
    main()