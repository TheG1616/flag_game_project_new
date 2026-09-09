from importlib.metadata.diagnose import run

import pygame
import consets
import screen
import game_field
import solider
run = True


def main():
    pygame.init()
    pygame.display.set_caption("The_Flag_Game")
    board = game_field.generate_random_dungeon()
    player_r = 3
    player_c = 0


    screen.screen.fill(consets.BACKGROUNDE_COLOR)
    screen.drow_grass()

    screen.drow_mode_night(game_field.generate_random_dungeon())
    while run:
        player_r, player_c, mine, flag = handle_user_events(board, player_r,
                                                            player_c)
        if mine:
            print("Mine")
        screen.drow_game(player_r * consets.CELL_SIZE, player_c * consets.CELL_SIZE)






def handle_user_events(board, player_r, player_c):
    mine = False
    flag = False
    global run
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            dr, dc = 0, 0
            if event.key == pygame.K_KP_ENTER:
                pass
            elif event.key == pygame.K_UP:
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