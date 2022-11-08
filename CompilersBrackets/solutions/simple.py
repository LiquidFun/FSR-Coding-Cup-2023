# Author: Brutenis Gliwa

from itertools import accumulate
s = [1 if c == "{" else -1 for c in input()]
print("invalid" if any(a < 0 for a in accumulate(s)) or sum(s) != 0 else "valid")
