rows, cols = map(int, input().split())
assert 3 <= rows <= 100 
assert 3 <= cols <= 200 
maze = [list(input()) for _ in range(rows)]
assert len(maze) == rows
assert all(len(row) == cols for row in maze)
as_str = ''.join(sum(maze, []))
assert all(c in '#.' for c in as_str)
for y in range(rows):
    for x in range(cols):
        if x == 0 or x == cols-1 or y == rows-1:
            assert maze[y][x] == '#'
