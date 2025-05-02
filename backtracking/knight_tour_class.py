
class KnightsTour:
    MOVES = (
        (-1, -2), (+1, -2),
        (-1, +2), (+1, +2),
        (-2, -1), (-2, +1),
        (+2, -1), (+2, +1),
    )

    def __init__(self, x: int, y: int, rows: int, cols: int) -> None:
        self.x = x
        self.y = y
        self.rows = rows
        self.cols = cols

        self.moves_count = 1

        self.highest_moves_count = 0
        self.failed_board = None


        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.board[x][y] = '0'

    def print_board(self, board=None) -> None:
        if board is None:
            board = self.board

        print('-----' * len(self.board[0]))
        for row in board:
            for col in row:
                print(f'| {col} ', end=' ')
            print('|')
            print('-----' * len(self.board[0]))

    def check_valid_moves(self, new_x: int, new_y: int) -> bool:
        return (
            0 <= new_x < self.rows and
            0 <= new_y < self.cols and
            self.board[new_x][new_y] == ' '
        )

    def move_knight(self, x: int, y: int) -> bool:

        if self.moves_count == self.rows * self.cols:
            self.print_board()
            # self.print_board(self.failed_board)
            print(f'Moves needed: {self.moves_count}')
            return True

        for dx, dy in self.MOVES:
            new_x, new_y = x + dx, y + dy

            if self.check_valid_moves(new_x, new_y):
                self.board[new_x][new_y] = str(self.moves_count)
                self.moves_count += 1

                if self.move_knight(new_x, new_y):
                    return True

                self.board[new_x][new_y] = ' '
                self.moves_count -= 1

            if self.moves_count > self.highest_moves_count:
                self.highest_moves_count = self.moves_count
                self.failed_board = [row[:] for row in self.board]

        return False

    def start_program(self) -> None:
        if not self.move_knight(self.x, self.y):
            print('Failed to check all cells')
            print(f'Moves made: {self.highest_moves_count}')
            print('Latest board state:')
            self.print_board(self.failed_board)



Knights = KnightsTour(0, 0, 5, 5)

Knights.start_program()
