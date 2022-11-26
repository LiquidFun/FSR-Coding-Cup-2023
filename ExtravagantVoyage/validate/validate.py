N, V = map(int, input().split())
volumes = [int(a) for a in input().split()]
values = [int(a) for a in input().split()]

assert 1 <= V <= 1000
assert 1 <= N == len(volumes) == len(values)
assert all(1 <= v <= 1000 for v in volumes)
assert all(1 <= v <= 100 for v in values)

try:
    input()
    raise Exception("Did not expect another line")
except EOFError:
    pass
