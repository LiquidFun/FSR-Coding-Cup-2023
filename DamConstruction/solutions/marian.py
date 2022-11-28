# Author: Marian Zuska

w = int(input())
b1, b2, b4 = map(int, input().split())

height = 0
while True:

    w4 = min(b4, w//4)
    wr = w - 4*w4
    w2 = min(b2, wr//2)
    wr = wr-2*w2
    w1 = min(b1, wr)
    wr = wr - w1
    if wr > 0:
        break

    curHeight = 10000000000000
    if w4 > 0:
        curHeight = min(curHeight, b4 // w4)
    if w2 > 0:
        curHeight = min(curHeight, b2 // w2)
    if w1 > 0:
        curHeight = min(curHeight, b1 // w1)

    height += curHeight
    b4 -= curHeight * w4
    b2 -= curHeight * w2
    b1 -= curHeight * w1

print(height)