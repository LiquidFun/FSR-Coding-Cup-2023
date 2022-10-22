n = int(input())
current = [int(a) for a in input().split()]
target = [int(a) for a in input().split()]

total = 0
for i in range(len(current)-1):
    diff = target[i] - current[i]
    total += min(10 - abs(diff), abs(diff))
    current[i+1] = (current[i+1] + diff) % 10
    
print(total if current[-1] == target[-1] else "impossible")
