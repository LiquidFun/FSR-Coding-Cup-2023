import sys
lines = sys.stdin.readlines()
assert len(lines) == 1
a, b, c = map(int, lines[0].split())
assert 1 <= a <= 1000
assert 1 <= b <= 50
assert 1 <= c <= 999
