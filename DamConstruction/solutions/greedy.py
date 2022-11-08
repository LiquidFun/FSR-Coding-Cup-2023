# Author: Brutenis Gliwa

target_width = int(input())
bricks = list(reversed([int(a) for a in input().split()]))
sizes = [4, 2, 1]

height = 0
while True:
    curr_width = target_width
    max_possible = 1e9
    to_be_used = []
    for i, size in enumerate(sizes):
        to_be_used.append(min(bricks[i], curr_width // size))
        if to_be_used[-1] != 0:
            max_possible = min(max_possible, bricks[i] // to_be_used[-1]) 
        curr_width -= size * to_be_used[-1]

    # print(target_width, height, max_possible, bricks, to_be_used)
    if curr_width != 0:
        break
    for i, u in enumerate(to_be_used):
        bricks[i] -= max_possible * u
    height += max_possible
print(height)
