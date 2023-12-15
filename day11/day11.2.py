file1 = open('input.txt', 'r')
Lines = file1.readlines()

universe = []

for line in Lines:
    if line[-1] == "\n":
        line = line[0:-1]
    universe.append(line)

def print_universe(uni):
    for r in uni:
        print(r)

print_universe(universe)

n = len(universe)
m = len(universe[0])

# Expand the universe
empty_rows = [0 for _ in range(m)]
empty_cols = [1 for _ in range(m)]

# Expand the universe
galaxy = []

for i in range(n):
    for j in range(m):
        if universe[i][j] == "#":
            galaxy.append((i, j))
            empty_cols[j] = 0

    if universe[i] == "." * m:
        empty_rows[i] = 1

empty_rows = list(empty_rows)
empty_cols = list(empty_cols)

k = len(galaxy)

ans = 0

for i in range(k):
    for j in range(i+1, k):
        start_row, start_col = galaxy[i]
        end_row, end_col = galaxy[j]

        num_row_space = sum(empty_rows[start_row:end_row]) if start_row < end_row else sum(empty_rows[end_row:start_row])
        num_col_space = sum(empty_cols[start_col:end_col]) if start_col < end_col else sum(empty_cols[end_col:start_col])

        dist = abs(start_col - end_col) + abs(start_row - end_row) + 999999*num_row_space + 999999*num_col_space

        ans += dist
        # print(f"{i} {j}: {dist}")
        # print(f"{num_row_space} {num_col_space}")

print(ans)