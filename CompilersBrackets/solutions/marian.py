# Author: Marian Zuska

s = 0
string = input()
for b in string:
    s += 1 if b == "{" else -1
    if s < 0:
        break
if s == 0:
    print("valid")
else:
    print("invalid")
