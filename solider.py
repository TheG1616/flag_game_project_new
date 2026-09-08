import consets


def move_solider(board, player_r, player_c, dr, dc):
    flag = False
    mine = False
    if check_board_limit(board, player_r, player_c, dr, dc):
        new_player_r = player_r + dr
        new_player_c = player_c + dc
        if step_on_flag(board, new_player_r, new_player_c):
            flag = True
        elif step_on_mine(board, new_player_r, new_player_c):
            mine = True

        return new_player_r, new_player_c, mine,flag
    else:
        return player_r, player_c, mine,flag




def check_board_limit(board, player_r, player_c, dr, dc):
        if player_r - 3 + dr < 0 or player_c + dc < 0 or player_c + consets.SOLDIER_COLS -1+ dc >consets.BOARD_COLS or player_r+dr > consets.BOARD_ROWS:
            return False

        return True



def step_on_flag(board, player_r, player_c):
    for i in range(1,consets.SOLDIER_BODY_ROWS+1):
        for j in range(consets.SOLDIER_COLS):
            if board[player_r - i][player_c + j] == "flag":
                return True

    return False

def step_on_mine(board, player_r, player_c):
    for i in range(consets.SOLDIER_COLS):
        if board[player_r][player_c+i] == "mine":
            return True

    return False



