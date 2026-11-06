from ttt_funcs import draw_grid
from ttt_funcs import get_pl_moves
from ttt_vars import playing_grid,win_combo,grid_pos

draw_grid()

while True:
    get_pl_moves()

    for i in win_combo:
        if all(playing_grid[r][c] == "X" for r,c in i):
            print("WIN!")
            break
    else:
        continue

    break
