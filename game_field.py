import consets
import random

import solider


def generate_random_dungeon():
    board = []
    for row in range(consets.BOARD_ROWS):
        row = []
        for col in range(consets.BOARD_COLS):
            row.append("empty")

        board.append(row)

    return generate_flag_and_mines(board)


def generate_mines(board, flag_row_index, flag_col_index):
    mine_count = consets.MINES_COUNT
    mine_row = consets.MINE_ROWS
    mine_col = consets.MINE_COLS
    for i in range(mine_count):
        while True:
            row = random.randint(0, consets.BOARD_ROWS - 1)
            col = random.randint(0, consets.BOARD_COLS - 1)
            if check_available_mines(board, row, col, mine_row, mine_col):
                break

        for k in range(mine_row):
            for l in range(mine_col):
                board[row + k][col + l] = "mine"



    return board

def check_available_mines(board, row, col,mine_row,mine_col):
    for i in range(mine_row):
        for j in range(mine_col):
            try:
                if board[row + i][col + j] != "empty":
                    return False
            except IndexError:
                return False

    return True



def generate_flag_and_mines(board):
    flag_row_index = consets.flag_row
    flag_col_index = consets.flag_col

    for i in range(consets.FLAG_ROWS):
        for j in range(consets.FLAG_COLS):
            board[flag_row_index + i][flag_col_index + j] = "flag"

    board = generate_mines(board, flag_row_index, flag_col_index)
    return board


board = generate_random_dungeon()
for row in board:
    print(row)


# ro = int(input("row"))
# co = int(input("col"))
# print(solider.move_solider(board,3,0,ro,co))
