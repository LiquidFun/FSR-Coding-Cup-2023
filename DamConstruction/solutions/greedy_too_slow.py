# Author: Brutenis Gliwa

target_width = int(input())
bricks = list(reversed([int(a) for a in input().split()]))
sizes = [4, 2, 1]

height, curr_width = -1, 0
while curr_width == 0:
    height += 1
    curr_width = target_width
    for i, size in enumerate(sizes):
        to_be_used = min(bricks[i], curr_width // size)
        curr_width -= size * to_be_used
        bricks[i] -= to_be_used
print(height)
