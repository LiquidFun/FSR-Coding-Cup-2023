# Author: Marian Zuska
# 2D dp solution
# Either use @lrucache (automatic dp) or commented out code

import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

n, v = map(int, input().split())
dp = [[-1 for _ in range(n+2)] for _ in range(v+2)]
volumes = list(map(int, input().split()))
scores = list(map(int, input().split()))


@lru_cache(None)
def solve(n,v):
    if v < 0:
        return -1e9
    if n == 0:
        return 0
    # if dp[v][n] != -1:
    #     return dp[v][n]
    score = max(solve(n-1, v), scores[n-1] + solve(n-1, v - volumes[n-1]))
    # dp[v][n] = score
    return score


print(solve(n, v))
