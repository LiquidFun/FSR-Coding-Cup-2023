# Author: Brutenis Gliw:

from queue import PriorityQueue

kb = [input() for _ in range(6)]
chars = input()

DEBUG_OUTPUT = False
if DEBUG_OUTPUT:
    print('\n'.join(kb))
    print(chars)

def dist(yx1, yx2):
    return abs(yx1[0] - yx2[0]) + abs(yx1[1] - yx2[1])

char_to_coord = {c: (y, x) for y, row in enumerate(kb) for x, c in enumerate(row)}
distances = {(c1, c2): dist(yx1, yx2) for c1, yx1 in char_to_coord.items() for c2, yx2 in char_to_coord.items()}

queue = PriorityQueue()
queue.put((0, 0, (0, 0), 0, (0, 0), 0))
visited = set()

def print_tup(tup, tab=False):
    t, index, pos1, rem1, pos2, rem2 = tup
    if rem2 < rem1:
        pos1, rem1, pos2, rem2 = pos2, rem2, pos1, rem1
    print(f"  {'+ ' if tab else '  '}{t:2} {index:3}", " | ",  pos1, kb[pos1[0]][pos1[1]], f"{rem1:3}", " | ", pos2, kb[pos2[0]][pos2[1]], f"{rem2:3}")

best = 1e100
while not queue.empty():
    t, index, pos1, rem1, pos2, rem2 = queue.get()
    tup = (index, pos1, rem1, pos2, rem2)
    if t >= best:
        break
    if tup in visited:
        continue
    visited.add(tup)
    if rem2 < rem1:
        pos1, rem1, pos2, rem2 = pos2, rem2, pos1, rem1
    #print_tup((t, *tup))

    if -index == len(chars):
        best = min(best, t + max(rem1, rem2))
        continue

    tpos = char_to_coord[chars[-index]]
    d1 = dist(pos1, tpos)
    d2 = dist(pos2, tpos)

    #print_tup((t + rem2, index-1, tpos, max(d1+rem1-rem2, 0), pos2, 0), True)
    queue.put((t + rem2, index-1, tpos, max(d1+rem1-rem2, 0), pos2, 0))
    #print_tup((t + rem2 + d2, index-1, pos1, rem1-rem2-d2, tpos, 0), True)
    queue.put((t + rem2 + d2, index-1, pos1, rem1-rem2-d2, tpos, 0))
    #print()

print(best)
