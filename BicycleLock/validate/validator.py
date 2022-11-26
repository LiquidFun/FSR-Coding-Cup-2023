n = int(input())
current = list(map(int, input().split()))
target = list(map(int, input().split()))
assert 2 <= n == len(current) == len(target) <= 100
assert all(0 <= a <= 9 for a in (target + current))

