import string
allowed = string.ascii_letters + ":' "

n = int(input())
assert 1 <= n <= 50
for _ in range(n):
    book = input()
    assert 1 <= len(book) <= 100
    assert all(c in allowed for c in book)

