mf, grow, fish = [int(a) for a in input().split()]
grow = 1 + grow / 1000
fish = 1 - fish / 1000

possible = []
for i in range(1, 366):
    if (remaining := grow**i * fish**(365-i)) >= 1:
        possible.append((grow**i - remaining) * mf)
print(max(possible))
