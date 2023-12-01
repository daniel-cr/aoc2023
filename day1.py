#!/usr/bin/env python3

# Part 1
import re
ans = 0
with open('day1.txt', 'r') as data:
    for line in data:
        output = re.sub(r'[a-z]', '', line)
        ans += int(output[0]) * 10 + int(output[-2])

print(ans)

# Part 2
d = {
    'o': ["one"],
    't': ["two", "three"],
    'f': ["four", "five"],
    's': ["six", "seven"],
    'e': ["eight"],
    'n': ["nine"],
    'z': ["zero"]
}

bd = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}


def check(r):
    for i in r:
        if line[i].isdigit():
            return int(line[i])
        
        if line[i] in d:
            for temp in d[line[i]]:
                if len(temp) + i - 1 >= n:
                    break
                s = line[i: i + len(temp)]
                if s in bd.keys():
                    return bd[s]

ans = 0
with open('day1.txt', 'r') as data:
    for line in data:
        line = line.strip()
        n = len(line)
        
        ans += 10 * check(range(n)) + check(range(n-1, -1, -1))
            
print(ans)