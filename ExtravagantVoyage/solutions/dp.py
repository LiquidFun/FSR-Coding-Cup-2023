n, v = map(int, input().split())
volume = [int(a) for a in input().split()]
value = [int(a) for a in input().split()]

dp = [0] + [-1] * v
for v, s in zip(volume, value):
    for i in range(len(dp)):
        if dp[i] != -1 and i+v < len(dp):
            dp[i+v] = max(dp[i+v], dp[i]+s)
print(max(dp))

