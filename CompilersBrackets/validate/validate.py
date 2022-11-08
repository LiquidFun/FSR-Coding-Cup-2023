brackets = input()
assert 1 <= len(brackets) <= 1000
assert all(s in "{}" for s in brackets)
