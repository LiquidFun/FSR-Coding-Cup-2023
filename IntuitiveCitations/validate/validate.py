import string

def assure_naming(name):
    assert 2 <= len(name) <= 20 
    assert name[0] in string.ascii_uppercase
    assert all(c in string.ascii_lowercase for c in name[1:])

n = int(input())
assert 1 <= n <= 50
for i in range(n):
    list(map(assure_naming, input().split()))

