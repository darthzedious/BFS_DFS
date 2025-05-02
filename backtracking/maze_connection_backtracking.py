import random

PATH = 'X'
WALL = '*'
VISITED = ' '

row = 11
col = 11

board = [['X' if i % 2 != 0 and j % 2 != 0 else '*' for i in range(col)] for j in range(row)]

dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]

def is_valid_coords(x, y):
    return (
            1 <= x < row and
            1 <= y < col and
            board[x][y] == 'X'
    )

def print_board(board) -> None:

    print('-----' * len(board))
    for row in board:
        for col in row:
            print(f'| {col} ', end=' ')
        print('|')
        print('-----' * len(board))

# print_board(board)

def wall_breaking(x, y):
    board[x][y] = VISITED
    directions = [(x, y+2), (x, y-2), (x+2, y), (x-2, y)]
    random.shuffle(directions)

    for dir_x, dir_y in directions:
        if is_valid_coords(dir_x, dir_y):
            board[(x +dir_x)//2][(y + dir_y)//2] = VISITED

            wall_breaking(dir_x, dir_y)


wall_breaking(1, 1)
print_board(board)
