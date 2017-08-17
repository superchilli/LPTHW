'''

'''

import random

words = []

with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.read(line).strip()
        words.append(line)

index=random.randint(range(len(words)))

print('randomword: ', words[index])
