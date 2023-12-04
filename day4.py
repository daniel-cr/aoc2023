#!/usr/bin/env python3

import utils

filename = "day4.txt"

data = utils.read_file(filename)
ans = 0
for line in data:
    a, b = line.split(':')[1].split('|')
    a, b = a.split(), b.split()
    value = len(set(a).intersection(set(b)))
    if value:
        ans += 2 ** (value - 1)
print(ans)


n = len(data)
d = [1 for _ in range(n)]

for i, line in enumerate(data):
    a, b = line.split(':')[1].split('|')
    a, b = a.split(), b.split()
    value = len(set(a).intersection(set(b)))
    if value:
        for j in range(value):
            if i + j + 1 < n:
                d[i + j + 1] += d[i]
print(sum(d))