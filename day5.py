
from functools import reduce

filename = "day5.txt"

f = open(filename).read().rstrip()
blocks = f.split('\n\n')
seeds = list(map(int, blocks[0].split(':')[1].split()))

b_maps = []
for block in blocks[1:]:
    map_to = []
    for xyz in block.split('\n')[1:]:
        x, y, z = map(int, xyz.split())
        map_to.append([y, x, z])
    map_to.sort()
    b_maps.append(map_to)

def f_min(curr, map_to):
    for y, x, z in map_to:
        if curr > y + z - 1:
            continue
        if curr < y:
            return curr
        return curr + x - y
    return curr

best = 10 ** 13
for s in seeds:
    curr = s
    for m in b_maps:
        curr = f_min(curr, m)
    best = min(curr, best)
print(best)


seed_range = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
seed_range = [[sa, sa + sb] for sa, sb in seed_range]

def split_range(a, b, m):
    n_range = []
    for y, x, z in m:
        left, right = y, y + z - 1
        span = x - y
        if a > right or b < left:
            continue
        if a < left:
            a1, b1 = a, left - 1
            a2, b2 = x, min(right, b) + span
            n_range.extend([(a1, b1), (a2, b2)])
        else:
            a3, b3 = a + span, min(right, b) + span
            n_range.append((a3, b3))
        if right > b:
            return n_range
        a = y + z - 1
    return n_range if n_range else [(a, b)]


ans = 10 ** 13
for s in seed_range:
    curr = [[*s]]
    for m in b_maps:
        pos = []
        for s, t in curr:
            pos += split_range(s, t, m)
        curr = pos
    ans = min(ans, min(curr)[0])
print(ans)


# brtf
# ans = 10 ** 13
# n = 100000000

# seed_range = [seed_range[2]]

# import numpy as np
# for i, (sa, sb) in enumerate(seed_range):

#     f = list(map(int, np.linspace(sa, sb, n)))
#     t = min([reduce(f_min, b_maps, s) for s in f])
#     ans = min(t, ans)
#     print(i, t)
# print(ans)
