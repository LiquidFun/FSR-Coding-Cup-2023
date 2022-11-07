import string

n = int(input())
words = input().split()

assert 1 <= len(words) == n <= 1000
assert all(1 <= len(w) <= 50 for w in words)
assert all(all(c in string.ascii_lowercase for c in w) for w in words)

