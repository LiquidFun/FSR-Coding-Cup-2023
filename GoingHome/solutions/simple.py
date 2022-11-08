# Author: Brutenis Gliwa

from queue import PriorityQueue
from collections import defaultdict

edges = {}
connections = defaultdict(list)

_, edge_count, finish = input().split()
for _ in range(int(edge_count)):
    fr, to, travel, _, *times = input().split()
    times = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in times]
    edges[(fr, to)] = (int(travel), times)
    connections[fr].append(to)

def fmt_mins(mins):
    return f"{mins//60:02}:{mins%60:02}"

queue = PriorityQueue()
queue.put((0, "rostock"))
visited = set()
while not queue.empty():
    time, curr = queue.get()
    if curr == finish:
        print(fmt_mins(time))
        exit(0)
    visited.add(curr)
    for con in connections[curr]:
        if con not in visited:
            travel, times = edges[(curr, con)]
            try:
                queue.put((next(t for t in times if t >= time) + travel, con))
            except StopIteration:
                pass

print("impossible")

        
