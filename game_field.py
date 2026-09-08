from typing import Protocol

import consets
import random



def generate_random_dungeon():
    random_dungeon = []
    for row in range(consets.BOARD_ROWS):
        row = []
        for col in range(consets.BOARD_COLS):
            row.append("empty")

        random_dungeon.append(row)

    return random_dungeon


def create_random_mine(board):
    row = random.randint(0, consets.BOARD_ROWS - 1)
    col = random.randint(0, consets.BOARD_COLS - 1)
