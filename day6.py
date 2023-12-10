#!/usr/bin/env python3

import re
import math

filename = 'day6.txt'
f = open(filename).read().rstrip()

ans = list(map(int, re.findall(r"\d+",f)))
n = len(ans)
time, distance = ans[:n//2], ans[n//2:]

def quadr(time, distance):
    ans = 1
    for t, d in zip(time, distance):
        p = (t + math.sqrt(t ** 2 - 4 * d)) / 2
        q = (t - math.sqrt(t ** 2 - 4 * d)) / 2

        p, q = min(p, q), max(p, q)
        p, q = int(math.floor(p)), int(math.ceil(q))
        ans *= q - p - 1

    return ans

print('Part 1 : ', quadr(time, distance))


print('Part 2 : ', quadr(
    [int(''.join(map(str, time)))], [int(''.join(map(str, distance)))]))