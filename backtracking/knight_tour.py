# (x, y)
moves = (
    (-1, -2), (+1, -2),
    (-1, +2), (+1, +2),
    (-2, -1), (-2, +1),
    (+2, -1), (+2, +1),
)

def moves_validation(x, y, board):
    return (
        0 <= x < len(board) and
        0 <= y < len(board[0]) and
        board[x][y] == ' '
    )

def print_line(board):
    print('-----' * len(board[0]))

def print_board(board):
    print_line(board)
    for row in board:
        for col in row:
            print(f"| {col:2} ", end='')
        print('|')
        print_line(board)
    print()

def knight_tour(x, y, move_count, board, highest_moves_count, failed_board):

    if move_count == len(board) * len(board[0]):
        print("Solution Found:")
        print_board(board)
        return True

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if moves_validation(new_x, new_y, board):
            board[new_x][new_y] = move_count

            if knight_tour(new_x, new_y, move_count + 1, board, highest_moves_count, failed_board):
                return True


            if move_count > highest_moves_count[0]:
                highest_moves_count[0] = move_count
                failed_board[0] = [row[:] for row in board]

            board[new_x][new_y] = ' '

    return False


col = int(input("Enter the number of columns: "))
row = int(input("Enter the number of rows: "))

board = [[' ' for _ in range(col)] for _ in range(row)]

start_x = int(input("Enter the starting x coordinate: "))
start_y = int(input("Enter the starting y coordinate: "))

board[start_x][start_y] = '0'

highest_moves_count = [0]
failed_board = [[]]

if not knight_tour(start_x, start_y, 1, board, highest_moves_count, failed_board):
    print()
    print("No solution found.")
    print(f'Moves made: {highest_moves_count[0]}')
    print('Latest board state:')
    print_board(failed_board[0])
