import string

kb = [input() for _ in range(6)]
chars = input()
kbj = ''.join(kb)
assert len(set(kbj)) == 28

allowed = string.ascii_lowercase + "_"

assert set(kbj) == set(allowed + ".")
assert len(kb) == 6
assert len(kbj) == 36
assert kbj.count(".") == 36 - 27
assert 1 <= len(chars) <= 200
assert all(c in allowed for c in chars)
