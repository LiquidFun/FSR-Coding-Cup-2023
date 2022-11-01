rows, cols = map(int, input().split())
maze = [list(input()) for _ in range(rows)]

queue = [(0, x) for x in range(1, cols-1)]
while queue:
    (y, x) = queue.pop()
    if maze[y][x] == '.':
        maze[y][x] = 'w'
        for ya, xa in [(1, 0), (0, -1), (0, 1)]:
            queue.append((y+ya, x+xa))

print(sum(maze, []).count('w'))
