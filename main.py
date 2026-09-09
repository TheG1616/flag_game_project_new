from importlib.metadata.diagnose import run
from time import sleep

import pygame
import consets
import screen
import game_field
import solider
run = True


def main():
    global run
    pygame.init()
    screen.drow_start()
    board = game_field.generate_random_dungeon()
    player_r = 3
    player_c = 1

    screen.drow_grass()

    while run:



        player_r, player_c, mine, flag = handle_user_events(board, player_r,
                                                            player_c)
        if mine:
            screen.draw_lose_message()

        if flag:
            screen.draw_win_message()
            run = False

        screen.drow_game((player_r -3)* consets.CELL_SIZE , player_c * consets.CELL_SIZE)






def handle_user_events(board, player_r, player_c):
    mine = False
    flag = False
    global run
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False



        if event.type == pygame.KEYDOWN:
            dr, dc = 0, 0

            if event.key == pygame.K_SPACE:
                screen.drow_all_for_space_key(board, player_r, player_c)

            if event.key == pygame.K_UP:
                dr = -1
            elif event.key == pygame.K_DOWN:
                dr = 1
            elif event.key == pygame.K_LEFT:
                dc = -1
            elif event.key == pygame.K_RIGHT:
                dc = 1

            if dr != 0 or dc != 0:
                player_r, player_c, mine, flag = solider.move_solider(board,
                                                                      player_r,
                                                                      player_c,
                                                                      dr, dc)

    pygame.display.update()
    return player_r, player_c, mine, flag


if __name__ == '__main__':
    main()