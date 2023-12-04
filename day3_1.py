#!/usr/bin/env python3

from bisect import bisect_left
from collections import deque

import utils

filename = "day3.txt"

sym_pos = []
data = utils.read_file(filename)
for line in data:
    sym = []
    for j, c in enumerate(line):
        if c.isdigit():
            continue
        if c == '.':
            continue
        sym.append(j)
    sym_pos.append(sym)


def bin_ser(a, b, i):
    left, right = 0, len(sym_pos[i]) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a-1 <= sym_pos[i][mid] <= b+1:
            return True
        elif sym_pos[i][mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    return False

ans = 0

def check(a, b, i):
    if bin_ser(a, b, i):
        return True
    if i > 0 and sym_pos[i - 1] and bin_ser(a, b, i - 1):
        return True
    if i < len(sym_pos) - 1 and sym_pos[i + 1] and bin_ser(a, b, i + 1):
        return True
    return False
        
for i, line in enumerate(data):
    start_id, curr = None, ""

    for j, c in enumerate(line):
        if c.isdigit():
            if not start_id:
                start_id = j
            curr += c
            continue
        
        if not start_id:
            continue

        ans += check(start_id, j - 1, i) * int(curr)
        start_id, curr = None, ""

    if start_id:
        ans += check(start_id, len(line) - 1, i) * int(curr)
print(ans)

