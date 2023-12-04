import utils

filename = "day3.txt"

data = utils.read_file(filename)
m, n = len(data), len(data[0])
idx, curr = 0, ""

sym = []
w = {}
nums = {}

def add_and_reset():
    global curr, idx
    nums[idx] = int(curr)
    curr = ""
    idx += 1

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c.isdigit():
            curr += c
            w[i, j] = idx
            continue

        if c == "*":
            sym.append((i, j))

        if len(curr):
            add_and_reset()

    if len(curr):
        add_and_reset()


ans = 0
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

for y, x in sym:
    st = set()
    for i in range(8):
        yi, xi = y + dy[i], x + dx[i]
        if (yi, xi) in w:
            st.add(w[yi, xi])

    if len(st) == 2:
        v = list(st)
        ans += nums[v[0]] * nums[v[1]]
        
print(ans)