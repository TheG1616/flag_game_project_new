from importlib.metadata.diagnose import run

import pygame
import consets
import screen
import game_field

run = True


def main():
    pygame.init()
    pygame.display.set_caption("The_Flag_Game")
    x = 50
    y = 50
    vel = 5


    screen.screen.fill(consets.BACKGROUNDE_COLOR)
    screen.drow_grass()
    screen.drow_mines(game_field.generate_random_dungeon())

    while run:
        handle_user_events()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel

        if keys[pygame.K_RIGHT]:
            x += vel

        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel

        screen.drow_game()





def handle_user_events():
    global run
    pygame.time.delay(100)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.K_KP_ENTER:
            pass

    pygame.display.update()


if __name__ == '__main__':
    main()