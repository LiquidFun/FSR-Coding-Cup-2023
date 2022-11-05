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

ans = []
while not queue.empty():
    t, index, pos1, rem1, pos2, rem2 = queue.get()
    tup = (index, pos1, rem1, pos2, rem2)
    if tup in visited:
        continue
    visited.add(tup)
    if rem2 < rem1:
        pos1, rem1, pos2, rem2 = pos2, rem2, pos1, rem1

    if -index == len(chars):
        ans.append(t + max(rem1, rem2))
        continue

    tpos = char_to_coord[chars[-index]]
    d1 = dist(pos1, tpos)
    d2 = dist(pos2, tpos)

    queue.put((t + rem2, index-1, tpos, max(d1+rem1, rem2), pos2, 0))
    queue.put((t + rem2 + d2, index-1, pos1, -rem2-d2, tpos, 0))

print(min(ans))
