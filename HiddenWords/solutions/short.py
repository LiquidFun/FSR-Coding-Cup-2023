_, w = input(),  input().split() + ['']
print(''.join([a[:i] for i in range(999) if b.startswith(a[i:])][0] for a,b in zip(w,w[1:])))

