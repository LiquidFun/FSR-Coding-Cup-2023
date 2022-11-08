# Author: Brutenis Gliwa

n, h = map(int, input().split())
accum_time = penalty = solved = 0
for time in sorted([int(input()) for _ in range(n)]):
    if penalty + time <= h * 60:
        accum_time += time
        penalty += accum_time
        solved += 1
print(solved, penalty)
