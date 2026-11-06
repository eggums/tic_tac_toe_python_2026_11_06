# TIC TAC TOE GAME(PYTHON)

## Idea
The tic tac toe game (ttt_game) I made was made to practice my programming skills and get familiar with the Python syntax.

I split the program into 3 files, ***ttt_game***, ***ttt_funcs*** and ***ttt_vars***.
This made the project easier to manage and organise/modify.

## ttt_vars

In this file I defined global variables which other function can use and manipulate.

I defined, the ***playing grid***, ***win combination*** and a dictionary which stores the, ***legal moves*** and links them to a coordinate on the playing grid stored as a tuple.

```python 
playing_grid = [
        [' ', 'A', 'B', 'C'],
        [1, 0, 0, 0],
        [2, 0, 0, 0],
        [3, 0, 0, 0]
    ]

grid_pos = {

    "A1": (1,1),
    "A2": (2,1),
    "A3": (3,1),
    "B1": (1,2),
    "B2": (2,2),
    "B3": (3,2),
    "C1": (2,3),
    "C2": (2,3),
    "C3": (3,3),

}

win_combo = [

    # X
    [(1,1), (1,2), (1,3)],
    [(2,1), (2,2), (2,3)],
    [(3,1), (3,2), (3,3)],

    # Y
    [(1,1), (2,1), (3,1)],
    [(1,2), (2,2), (3,2)],
    [(1,3), (2,3), (3,3)],

    # D
    [(1,1), (2,2), (3,3)],
    [(1,3), (2,2), (3,1)]

]
```
So, in dictionary grid_pos, key ***A1*** is assigned to ***tuple (1,1)*** and so on. Tuple (1,1) is set this way so when it unpacks, it would refer to element one of list one in playing_grid.
This is same for the other key and tuple pair.

***win_combo*** is a list of a list of tuples that are all wining combinations. Each tuple is one square of the tic tac toe grid. Since there are 9 squares, there are ***3 horizontal***, ***3 vertical*** and ***2 diagonal*** win combinations.


## ttt_funcs

This file defines the main player actions.

There are 2 actions, ***get_pl_moves***(get player moves) and ***draw_grid***(draws the playing grid).

### get_pl_moves

gets the players move and stores it in a variable called, ***user_move***.

```python
def get_pl_moves():
    user_move = input("Please make a move: ")
```
Then, it checks if the vlaue the user has inputted is equivalent to any of the keys in dictionary grid_pos.

If so, it would print to the console, *"Valid Move"* and unpack the user's input held by user_move. It does this by, referring to the dictionary; grid_pos and sees which tuple is linked to the key identified by the variable, user_move. It then, unpacks that tuple by putting the first value of the tuple into the first variable given (in this case its 'r') and than it puts the second value of the tuple into the second variable given (in this case its 'c').

_(grid_pos will refer to the key, grid_pos[some_key] will refer to the value linked to that key, in this case a tuple which holds a coordinate of some square on playing_grid.)_

get_pl_moves now changes the playing grid by changing the values held at [r][c] to 'X'.

the updated playing_grid is then drawn with the function, draw_grid.

If the user's input stored in user_move was **NOT** a key in grid_pos, ttt_funcs would print *"Invalid Move !"* to the console and prompt the user to enter a move again until a valid move is made.


```python
def get_pl_moves():
    user_move = input("Please make a move: ")

    if user_move in grid_pos:
        print("Valid Move")

        r,c = grid_pos[user_move]
        playing_grid[r][c] = 'X'

        draw_grid()

    else:
        print("Invalid Move !")
```

## ttt_game

This functions is the main game loop. It checks for win conditions.

It first draws the playing_grid with the draw_grid function.
Than, the game loop begins with ***while True:***

``` python
while True:
    get_pl_moves()

    for i in win_combo:
        if all(playing_grid[r][c] == "X" for r,c in i):
            print("WIN!")
            break
```

The for loop checks ***every element*** in list win_combo (in this case, list of tuples containing coordinates of squares on the playing_grid that are in a specific combination that is condition for a win).
if all the squares in such a combination holds the value of *'X'* than print *"WIN!"* and break the loop, if not move to next instance till a win condition is satisfied.


```python
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
```

# SCREENSHOT

![screenshot_ttt_game.py](./2026-11-06-2053_ttt_game(python).png)
