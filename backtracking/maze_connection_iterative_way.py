import random

WALL = "W"
FLOOR = "F"
VISITED = "V"

ROWS = 11
COLS = 11

board = [[FLOOR if x % 2 != 0 and j % 2 != 0 else WALL for x in range(COLS)] for j in range(ROWS)]


def print_board(board) -> None:
    print('-----' * len(board))
    for row in board:
        for col in row:
            print(f'| {col} ', end=' ')
        print('|')
    print('-----' * len(board))


def is_valid(x, y):
    return (
            1 <= x < ROWS - 1 and
            1 <= y < COLS - 1 and
            board[x][y] == FLOOR
    )


def wall_breaking(x, y):

    visited_coordinates = []
    visited_coordinates.append((x, y))


    board[x][y] = VISITED


    while visited_coordinates:
        current_x, current_y = visited_coordinates[-1]


        directions = [
            (current_x, current_y + 2),
            (current_x, current_y - 2),
            (current_x + 2, current_y),
            (current_x - 2, current_y)
        ]

        random.shuffle(directions)

        found_new_path = False

        for dir_x, dir_y in directions:
            if is_valid(dir_x, dir_y):

                wall_x = (current_x + dir_x) // 2
                wall_y = (current_y + dir_y) // 2
                board[wall_x][wall_y] = VISITED

                board[dir_x][dir_y] = VISITED

                visited_coordinates.append((dir_x, dir_y))

                found_new_path = True
                break

        if not found_new_path:
            visited_coordinates.pop()


wall_breaking(1, 1)

print_board(board)
