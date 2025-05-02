import random

PATH  = '-'
WALL   = '#'
VISITED = ' '

height = 11
width = 11


maze = [[PATH if i % 2 != 0 and j % 2 != 0 else WALL for i in range(height)] for j in range(width)]

def print_maze():
    def print_line():
        for i in range(0, len(maze[0]) - 1):
            print('-----', end="")
        print('---')
    print_line()
    for row in maze:
        for el in row:
            print(f"| {el} ", end='')
        print('|')
        print_line()
    print()


def is_valid_coords(x, y):
    return 1 <= y < height and 1 <= x < width and maze[x][y] == PATH

def wall_breaking(x, y):
    maze[x][y] = VISITED
    directions = [(x, y+2), (x, y-2), (x+2, y), (x-2, y)]
    random.shuffle(directions)

    for dir_x, dir_y in directions:
        if is_valid_coords(dir_x, dir_y):
            maze[(x +dir_x)//2][(y + dir_y)//2] = VISITED

            wall_breaking(dir_x, dir_y)

wall_breaking(1, 1)
print_maze()