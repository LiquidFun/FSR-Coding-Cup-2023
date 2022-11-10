n = int(input())
names = [input() for _ in range(n)]
surnames = [name.split()[-1] for name in names]
surnames.sort()
print(surnames[0], "et al.")
