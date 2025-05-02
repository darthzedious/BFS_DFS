from queue import Queue

UNGND  = ' '  # marker for unvisited ground
VISGND = '-'  # visited ground
LAVA   = '#'  # lava -> can't step on it
TARGET = '$'  # target cell
WINSYM = '!' # symbol for the winning path

# the map of our maze
maze = [
    [' ', ' ', ' '],
    ['#', '#', ' '],
    ['$', ' ', ' '],
    ['#', '#', ' '],
    [' ', ' ', ' '],
]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # all possible directions in coordinate changes

def is_valid_coords(x, y):
    """
    Try to enter the cell with coordinates x, y.
    Can we step in this cell? It shall be inside the matrix and
    either unvisited ground or the target.
    """
    if x < 0 or y < 0:
        return False
    if x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == UNGND or maze[x][y] == TARGET:
        return True

    return False

def print_maze():
    # helper function for the contours of the maze
    def print_line():
        for i in range(0, len(maze[0]) - 1):
            print('-----', end="")
        print('---')
    # visualization of the current maze state
    print_line()
    for row in maze:
        for el in row:
            print(f"| {el} ", end='')
        print('|')
        print_line()
    print()

def maze_bfs_traversal(start_x, start_y):
    # check if starting point is reachable
    if maze[start_x][start_y] == LAVA:
        print("Can't start from this point!")
        return
    # mark the first step
    maze[start_x][start_y] = 1
    # queue for the BFS traversal - the "wave"
    wave = Queue()
    wave.put((start_x, start_y))
    # try to move in all directions
    while (not wave.empty()):
        x, y = wave.get()
        for dir in dirs:
            new_x, new_y = x + dir[0], y + dir[1]
            if is_valid_coords(new_x, new_y):
                # check if we have reached the target
                if maze[new_x][new_y] == TARGET:
                    maze[new_x][new_y] = WINSYM
                    return
                # mark the cell with the number of steps to reach it
                maze[new_x][new_y] = maze[x][y] + 1
                wave.put((new_x, new_y))


maze_bfs_traversal(0, 0)
print("The maze after BFS traversal:")
print_maze()
