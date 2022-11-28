# Author: Marian Zuska

n, h = map(int,input().split())
times = []
for _ in range(n):
    times.append(int(input()))

times.sort()
time_spent = 0
solved = 0
penalty = 0
for problem in times:
    time_spent += problem
    if time_spent <= 60*h:
        solved += 1
        penalty += time_spent

print(solved, penalty)
