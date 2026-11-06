from ttt_vars import playing_grid,grid_pos

def draw_grid():
    for row in playing_grid:
        for element in row:
            print(element, end=" ")
        print()


def get_pl_moves():
    user_move = input("Please make a move: ")

    if user_move in grid_pos:
        print("Valid Move")

        r,c = grid_pos[user_move]
        playing_grid[r][c] = 'X'

        draw_grid()

    else:
        print("Invalid Move !")
