import consets
import random



def generate_random_dungeon():
    board = []
    for row in range(consets.BOARD_ROWS):
        row = []
        for col in range(consets.BOARD_COLS):
            rand_val = random.random()
            if rand_val < 0.3:
                row.append("mine")
            else:
                row.append("empty")

        board.append(row)

    board = generate_flag(board)

    return board


def generate_flag(board):
    flag_row_index = consets.flag_row
    flag_col_index = consets.flag_col

    for i in range(consets.FLAG_ROWS):
        for j in range(consets.FLAG_COLS):
            board[flag_row_index+i][flag_col_index+j] = "flag"

    return board


board = generate_random_dungeon()
for row in board:
    print(row)