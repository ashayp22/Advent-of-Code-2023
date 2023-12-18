file1 = open('input1.txt', 'r')
Lines = file1.readlines()

steps = []

for line in Lines:
    split_line = line.split(" ")

    color = split_line[2]

    if color[-1] == "\n":
        color = color[0:-1]

    steps.append((split_line[0], int(split_line[1]), color))

# Find grid width, height

row = (0, 0)
col = (0, 0)
curr = (0, 0)

def applyDirection(pos, dir, amt):
    if dir == "U":
        return (pos[0] - amt, pos[1])
    elif dir == "L":
        return (pos[0], pos[1] - amt)
    elif dir == "D":
        return (pos[0] + amt, pos[1])
    return (pos[0], pos[1] + amt)

def printGrid(g):
    for row in g:
        print("".join(row))

for direction, amount, _ in steps:
    curr = applyDirection(curr, direction, amount)
    row = (min(row[0], curr[0]), max(row[1], curr[0]))
    col = (min(col[0], curr[1]), max(col[1], curr[1]))

row = (row[0] - 1, row[1] + 1)
col = (col[0] - 1, col[1] + 1)

n = row[1] - row[0] + 1
m = col[1] - col[0] + 1

grid = [["." for _ in range(m)] for _ in range(n)]

curr = (-row[0], -col[0])
grid[-row[0]][-col[0]] = 1

filled = 0

# Cover the border
for direction, amount, _ in steps:
    for _ in range(amount):
        curr = applyDirection(curr, direction, 1)
        grid[curr[0]][curr[1]] = "#"
        filled += 1

queue = [(0, 0)]
visited = set()
visited.add((0, 0))

# Flood fill to cover the outside
while len(queue) > 0:
    r, c = queue.pop(0)
    grid[r][c] = "#"

    for new_r, new_c in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
        if 0 <= new_r < n and 0 <= new_c < m and (new_r, new_c) not in visited and grid[new_r][new_c] == ".":
            queue.append((new_r, new_c))
            visited.add((new_r, new_c))


# Count . left in the grid
for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            filled += 1

printGrid(grid)
print(f"Filled: {filled}")
