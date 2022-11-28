# Author: Marian Zuska

n = int(input())
words = input().split()
last = words[0]
sentence = words[0]
for word in words[1:]:
    for i in range(len(last)+1):
        ending = last[i:]
        if word.startswith(ending):
            sentence += word[len(ending):]
            break
    last = word
print(sentence)
