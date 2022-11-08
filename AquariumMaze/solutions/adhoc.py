r, c = map(int, input().split())

grid = []
grid_cpy = []
for _ in range(r):
    line = input()
    grid.append(list(line))
    grid_cpy.append(list(line))


air = sum([sum([1 if x == "." else 0 for x in line]) for line in grid])

out = 0

for y in range(1,r):
    for x in range(c):
        if grid[y-1][x] == "#" and grid[y][x] == ".":
            grid[y][x] = "?"

    airBubble = False
    length = 0
    for x in range(c):

        if grid[y][x] == ".":
            airBubble = False
            for i in range(length):
                grid[y][x-i-1] = "."
            length = 0

        elif grid[y][x] == "?":
            if airBubble:
                length += 1
            else:
                grid[y][x] = "."

        elif grid[y][x] == "#":
            if airBubble:
                out += length
                for i in range(length):
                    grid[y][x-i-1] = "#"
                length = 0
            else:
                airBubble = True
                length = 0

print(air - out)
