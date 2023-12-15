file1 = open('input.txt', 'r')
Lines = file1.readlines()

adj_list = {}
dividers = {} # N, E, S, W

n = 0
m = 0

start = None

pos_to_chr = {}

for line in Lines:
    m = 0
    for l in line:
        if l == "\n":
            continue

        pos_to_chr[(n, m)] = l

        if l == "F":
            adj_list[(n, m)] = [(n+1, m), (n, m+1)]
        elif l == "7":
            adj_list[(n, m)] = [(n+1, m), (n, m-1)]
        elif l == "|":
            adj_list[(n, m)] = [(n-1, m), (n+1, m)]
        elif l == "J":
            adj_list[(n, m)] = [(n-1, m), (n, m-1)]
        elif l == "L":
            adj_list[(n, m)] = [(n-1, m), (n, m+1)]
        elif l == "-":
            adj_list[(n, m)] = [(n, m-1), (n, m+1)]
        elif l == "S":
            start = (n, m)

        if l == "F":
            dividers[(n, m)] = [False, True, True, False]
        elif l == "7":
            dividers[(n, m)] = [False, False, True, True]
        elif l == "|":
            dividers[(n, m)] = [True, False, True, False]
        elif l == "J":
            dividers[(n, m)] = [True, False, False, True]
        elif l == "L":
            dividers[(n, m)] = [True, True, False, False]
        elif l == "-":
            dividers[(n, m)] = [False, True, False, True]
        else:
            dividers[(n, m)] = [True, True, True, True]

        m += 1

    n += 1

queue = []

start_i, start_j = start

def check_bounds(a, b):
    return 0 <= a < n and 0 <= b < m

for i, j, good in [(start_i - 1, start_j, ["|", "F", "7"]), (start_i + 1, start_j, ["|", "J", "L"]), (start_i, start_j - 1, ["-", "L", "F"]), (start_i, start_j + 1, ["-", "7", "J"])]:
    for g in good:
        if check_bounds(i, j) and pos_to_chr[(i, j)] == g:
            queue.append(((i, j), 1))
            break

visited = set()
visited.add((start_i, start_j))

on_path = set()
on_path.add((start_i, start_j))

while len(queue) > 0:
    front, dist = queue.pop(0)
    on_path.add(front)

    for neighbor in adj_list[front]:
        if check_bounds(neighbor[0], neighbor[1]) and neighbor not in visited:
            queue.append((neighbor, dist + 1))
            visited.add(front)

# PART 2 -----------------------

# Open dividers for everything that isn't in the path
for i in range(n):
    for j in range(m):
        if (i, j) not in on_path:
            dividers[(i, j)] = [True, True, True, True]

stretched_dividers = {}
stretched_on_path = set([(c*2, d*2) for c, d in on_path])

for (i, j) in dividers:
    stretched_dividers[(i*2, j*2)] = dividers[(i, j)]

    if (i, j) in on_path:
        stretched_on_path.add((i*2, j*2))


stretched_dividers[(start_i, start_j)] = [False, False, False, False]

# Connect up left and right, top and bottom
for i in range(2*n):
    for j in range(2*m):
        if i % 2 == 0 and j % 2 == 0:
            continue

        if (i-1, j) in stretched_on_path and (i+1, j) in stretched_on_path and stretched_dividers[(i-1, j)][2] and stretched_dividers[(i+1, j)][0]:
            # Split up and down
            stretched_dividers[(i, j)] = [True, False, True, False]
        elif (i, j-1) in stretched_on_path and (i, j+1) in stretched_on_path and stretched_dividers[(i, j-1)][1] and stretched_dividers[(i, j+1)][3]:
            # Split left and right
            stretched_dividers[(i, j)] = [False, True, False, True]
        else:
            stretched_dividers[(i, j)] = [True, True, True, True]

queue = [(0, 0)]
visited = set()

visited.add((0, 0))
visited.add((start_i, start_j))

outside = set()

while len(queue) > 0:
    i, j = queue.pop(0)

    if i % 2 == 0 and j % 2 == 0:
        outside.add((i/2, j/2))

    for new_i, new_j, div in [(i-1, j, 0), (i, j+1, 1), (i+1, j, 2), (i, j-1, 3)]:
        if (new_i, new_j) not in visited and check_bounds(new_i, new_j) and stretched_dividers[(new_i, new_j)][div]:
            queue.append((new_i, new_j))
            visited.add((new_i, new_j))


total = n*m
good = len(on_path)
num_out = len(outside)

all = []

for a in range(2*n):
    row = []
    for b in range(2*m):
        if stretched_dividers[(a, b)] != [True, True, True, True]:
            row.append("*")
        elif (a, b) == (start_i*2, start_j*2):
            row.append("S")
        else:
            row.append("O")

    all.append(row)
    print("".join(row))

queue = [(0, 0)]
visited = set()
visited.add((0, 0))
visited.add((start_i*2, start_j*2))

ans = 0

while len(queue) > 0:
    i, j = queue.pop(0)

    if i % 2 == 0 and j % 2 == 0:
        ans += 1

    for new_i, new_j in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
        if (new_i, new_j) not in visited and 0 <= new_i < 2*n and 0 <= new_j < 2*m and all[new_i][new_j] == "O":
            queue.append((new_i, new_j))
            visited.add((new_i, new_j))

print(total - ans - good)
