# Author: Marian Zuska

n = int(input())
start = list(map(int, input().split()))
target = list(map(int, input().split()))

all_steps = 0
for i in range(n-1):
    steps = (target[i] - start[i])%10

    start[i + 1] = (start[i+1]+steps)%10
    all_steps += min(steps, 10-steps)

if target[-1] != start[-1]:
    print("impossible")
else:
    print(all_steps)
