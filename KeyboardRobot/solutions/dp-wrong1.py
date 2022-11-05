kb = [input() for _ in range(6)]
chars = input()
# no_subsequent_duplicates = [chars[0]]
# for i in range(1, len(chars)):
#     if chars[i-1] != chars[i]:
#         no_subsequent_duplicates.append(chars[i])
# chars = ''.join(no_subsequent_duplicates)

DEBUG_OUTPUT = True
if DEBUG_OUTPUT:
    print('\n'.join(kb))
    print(chars)

char_to_coordinate = {}
for y, row in enumerate(kb):
    for x, c in enumerate(row):
        if c != '.':
            char_to_coordinate[c] = (y, x)

assert len(char_to_coordinate) == 27

def dist(yx1, yx2):
    return abs(yx1[0] - yx2[0]) + abs(yx1[1] - yx2[1])

distances = {}
for c1, yx1 in char_to_coordinate.items():
    for c2, yx2 in char_to_coordinate.items():
        distances[(c1, c2)] = dist(yx1, yx2)

def make_empty(size):
    return [[100] * 36 for _ in range(size)]

dp = make_empty(11)
dp[0][0] = 0
pos1 = (0, 0)
mi, ma = 0, 0
for char in chars:
    mi2, ma2 = len(dp), 0
    dp_next = make_empty(len(dp) + 10)
    tpos = char_to_coordinate[char]
    tp = tpos[0] * 6 + tpos[1]
    # for t, curr in enumerate(dp):
    for t in range(mi, ma+1):
        curr = dp[t]
        for p2, remaining in enumerate(curr):
            if remaining != 100:
                # pos1 is not moving, can be moved freely. Last position has to be at char position
                # pos2 might be moving, will be there in 'remaining' s; its (to-be) position is recorded as index in 36
                pos2 = (p2 // 6, p2 % 6)
                d1 = dist(pos1, tpos)
                d2 = dist(pos2, tpos)
                p1 = pos1[0] * 6 + pos1[1]

                if remaining == 0:
                    # either can be moved
                    dp_next[t][p1] = d2
                    dp_next[t][p2] = d1


                # moving p1:
                dp_next[t+remaining][tp] = max(0, d1 - remaining)
                # moving p2:
                dp_next[t+remaining+d2][p1] = 0

                #if remaining <= 0:
                #    # either can be moved
                #    dp_next[t][p2] = remaining - d1
                #    dp_next[t][p1] = max(0, d2 + remaining)

                #if remaining >= 0:
                #    # moving p1:
                #    dp_next[t+remaining][p2] = max(d1 - remaining, 0)
                #    # moving p2 (after it has arrived):
                #    dp_next[t+remaining+d2][p1] = - remaining - d2

                mi2, ma2 = min(mi2, t), max(ma2, t+remaining+d2)
    mi, ma = mi2, ma2
    pos1 = char_to_coordinate[char]
    dp = dp_next

    if DEBUG_OUTPUT:
        indeces = [t for t, d in enumerate(dp) if min(d) != 100]
        ans = sorted([(t, min(d)) for t, d in enumerate(dp) if min(d) != 100], key=sum)
        best_t_index = ans[0][0]
        best_36 = sorted((d, i) for i, d in enumerate(dp[best_t_index]))
        q = best_36[0][1]
        coords = q // 6, q % 6
        print(char, coords, tpos, best_36[0][0], indeces[:20], "..." if len(indeces) > 20 else "")

answers = [i + min(pos) for i, pos in enumerate(dp) if min(pos) != 100]
if DEBUG_OUTPUT:
    ans_no_rem = [i for i, positions in enumerate(dp) if min(positions) != 100]
    print("w/o  remaining:", ans_no_rem[:30], "...")
    print("with remaining:", answers[:30], "...")
print(min(answers))
#for i, positions in enumerate(dp):
#    if any(t != 100 for t in positions):
#        print(i)
#        break
