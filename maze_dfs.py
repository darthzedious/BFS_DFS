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
dirs_chars = ['>', 'v', '<', '^']         # markers for the directions

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

def maze_dfs(x, y, dir_index):
    # simple way to pause between steps
    input()
    # check if we have reached the target
    if maze[x][y] == TARGET:
        maze[x][y] = WINSYM
        print_maze()
        return True
    # mark the current cell as visited from the direction we came
    maze[x][y] = dirs_chars[dir_index]
    print_maze()
    # try to move in all directions
    for dir_index, dir in enumerate(dirs):
        new_x, new_y = x + dir[0], y + dir[1]     # calculate the new coordinates
        if is_valid_coords(new_x, new_y):         # check if we can make step in this direction
            if maze_dfs(new_x, new_y, dir_index): # try to find path from there
                return True                       # if there is a path from this cell, then there is a path from the start

    maze[x][y] = VISGND               # if this step wasn't winning cut that path
    print_maze()

    # if there is no path from any of our neighbors, then there is no path from the current vertex
    return False


if maze_dfs(0, 0, 0):
    print("There is a path!")
else:
    print("There is NO path!")