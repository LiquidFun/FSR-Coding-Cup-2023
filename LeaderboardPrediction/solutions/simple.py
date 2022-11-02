accum_time = penalty = solved = 0
for time in sorted([int(input()) for _ in range(8)]):
    if penalty + time <= 230:
        accum_time += time
        penalty += accum_time
        solved += 1
print(penalty, solved)
