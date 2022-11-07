n = int(input())
words = input().split()
answer = [words[0]]

for word in words[1:]:
    for i in range(len(answer[-1])+1):
        if word.startswith(answer[-1][i:]):
            answer[-1] = answer[-1][:i]
            answer.append(word)
            break

print(''.join(answer))
