import string

n, m, target = input().split()
n = int(n)
m = int(m)
assert 2 <= n <= 200
assert 1 <= m <= 10000
cities = set()
for i in range(m):
    c1, c2, mins, tracks, *schedule = input().split()
    mins = int(mins)
    tracks = int(tracks)
    for s in schedule:
        assert len(s) == 5
        assert ":" in s
        ho, mi = map(int, s.split(":"))
        assert 0 <= ho <= 23 and 0 <= mi <= 59
        assert ho * 60 + mi + mins <= 24*60-1
    cities |= {c1, c2}
    assert 1 <= mins <= 24*60
    assert 1 <= tracks <= 20
for city in cities:
    assert all(c in string.ascii_lowercase for c in city)
    assert all(1 <= len(c) <= 10 for c in city)
assert len(cities) == n
assert target != "rostock"
assert "rostock" in cities

