# Author: Marian Zuska

n, v = map(int,input().split())
volumes = list(map(int,input().split()))
scores = list(map(int,input().split()))

dp = [-1 for _ in range(v+3)]
dp[0] = 0
for i in range(n):
    for j in range(v, -1, -1):
        if dp[j] >= 0 and j+volumes[i] <= v:
            dp[j+volumes[i]] = max(dp[j+volumes[i]], dp[j]+scores[i])

print(max(dp))
