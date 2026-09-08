import images

BACKGROUNDE_COLOR = (0,153,0)
Shrubs_color = (102,255,102)
BLACK = (0,0,0)


BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE


SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

FLAG_ROWS = 3
FLAG_COLS = 4
# game_field.py
flag_row = BOARD_ROWS - FLAG_ROWS
flag_col = BOARD_COLS - FLAG_COLS

MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

START_MSG = ("Welcome to The Flag game. "
                                            "Have Fun!")


#==============images===================
SOLIDER_IMG = "images/soldier.png"
GRASS_IMG = "images/grass.png"
MINE_IMG = "images/mine.png"
EXPLOTION_IMG = "images/explotion.png"
INJURY_ING = "images/injury.png"
TELEPORT_ING = "images/teleport.png"
SNAKE_IMG = "images/snake.png"
GUARD_IMG = "images/guard.png"
FLAG_IMG = "images/flag.png"
SOLDIER_NIGHT_IMG = "images/soldier_night.png"



LOSE_MESSAGE = "You Lose"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

WIN_MESSAGE = "You Win"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
