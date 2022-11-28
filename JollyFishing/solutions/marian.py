# Author: Marian Zuska

a, b, c = map(int, input().split())

best = 0
for start_day in range(366):
    fish = a
    caught_fish = 0.0
    for day in range(365):
        if day >= start_day:
            caught_fish += fish * c/1000.0
            fish *= 1.0 - c/1000.0
        else:
            fish *= 1.0 + b/1000.0
    if fish >= a:
        best = max(best, caught_fish)

print(best)
