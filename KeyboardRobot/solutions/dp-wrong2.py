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
    return [{} for _ in range(size)]

dp = make_empty(11)
dp[0][(0, 0)] = (0, 0)
pos1 = (0, 0)
mi, ma = 0, 0
for char in chars:
    dp_next = make_empty(len(dp) + 10)
    tpos = char_to_coordinate[char]
    tp = tpos[0] * 6 + tpos[1]
    for t, curr in enumerate(dp):
        curr = dp[t]
        for (p1, p2), (rem1, rem2) in curr.items():
            if rem2 < rem1:
                p1, rem1, p2, rem2 = p2, rem2, p1, rem1
            assert rem2 >= 0 and rem1 <= rem2, f"{rem1} > {rem2}"
            # pos1 is not moving, can be moved freely. Last position has to be at char position
            # pos2 might be moving, will be there in 'remaining' s; its (to-be) position is recorded as index in 36
            pos1 = (p1 // 6, p1 % 6)
            pos2 = (p2 // 6, p2 % 6)
            d1 = dist(pos1, tpos)
            d2 = dist(pos2, tpos)

            #queue.put((t + rem2, index-1, tpos, max(d1+rem1, rem2), pos2, 0))
            #queue.put((t + rem2 + d2, index-1, pos1, -rem2-d2, tpos, 0))

            # moving p1:
            dp_next[t+rem2][(tp, p2)] = (max(d1+rem1, rem2), 0)
            # moving p2:
            dp_next[t+rem2+d2][(p1, tp)] = (-rem2-d2, 0)

    dp = dp_next

    if DEBUG_OUTPUT:
        indeces = [t for t, d in enumerate(dp) if d]
        ans = sorted([(t, min(map(max, pos.values()))) for t, pos in enumerate(dp) if pos], key=sum)
        best_t_index = ans[0][0]
        _, bv, (bk1, bk2), bi = sorted((max(v), v, k, i) for i, (k, v) in enumerate(dp[best_t_index].items()))[0]
        ck1 = bk1 // 6, bk1 % 6
        ck2 = bk2 // 6, bk2 % 6
        print(char, ck1, ck2, bv, indeces[:20], "..." if len(indeces) > 20 else "")

answers = [i + min(map(max, pos.values())) for i, pos in enumerate(dp) if pos]
if DEBUG_OUTPUT:
    ans_no_rem = [i for i, positions in enumerate(dp) if positions]
    print("w/o  remaining:", ans_no_rem[:30], "...")
    print("with remaining:", answers[:30], "...")
print(min(answers))
#for i, positions in enumerate(dp):
#    if any(t != (100, 100) for t in positions):
#        print(i)
#        break
