# Author: Brutenis Gliwa

import sys

surnames = [n.split()[1] for n in sys.stdin.readlines()[1:]]

print(sorted(surnames)[0], "et al.")
