#!/usr/bin/env python3

# Part 1
MX_RED, MX_GREEN, MX_BLUE = 12, 13, 14

def check_game_line(game_line):
    for sub_game in game_line.split(':')[1].split(';'):
        rgb = sub_game.split(',')

        for s in rgb:
            value, color = s.split()[:2]
            value = int(value)
            if color[0] == 'r' and value > MX_RED:
                return False
            if color[0] == 'g' and value > MX_GREEN:
                return False
            if color[0] == 'b' and value > MX_GREEN:
                return False
    return True

ans = 0
with open('day2.txt', 'r') as data:
    for i, game_line in enumerate(data):
        if check_game_line(game_line):
            ans += i + 1
print(ans)

# Part 2
ans = 0
with open('day2.txt', 'r') as data:
    for i, game_line in enumerate(data):
        mr, mg, mb = 0, 0, 0
        for sub_game in game_line.split(':')[1].split(';'):
            rgb = sub_game.split(',')

            for s in rgb:
                value, color = s.split()[:2]
                value = int(value)
                match color[0]:
                    case 'r':
                        mr = max(mr, value)
                    case 'g':
                        mg = max(mg, value)
                    case 'b':
                        mb = max(mb, value)
        ans += mr * mg * mb
print(ans)