# Author: Brutenis Gliwa

rows, cols = map(int, input().split())
maze = [list(input()) for _ in range(rows)]

def explore(x, y=0):
    if maze[y][x] == '.':
        maze[y][x] = 'w'
        for ya, xa in [(1, 0), (0, -1), (0, 1)]:
            explore(x+xa, y+ya)

list(map(explore, range(1, cols-1)))
print(sum(maze, []).count('w'))
