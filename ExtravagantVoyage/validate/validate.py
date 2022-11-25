N, V = map(int, input().split())
volumes = [int(a) for a in input().split()]
values = [int(a) for a in input().split()]

assert N == len(volumes) == len(values)
assert all(1 <= v <= 1000 for v in volume)
assert all(1 <= v <= 100 for v in values)
