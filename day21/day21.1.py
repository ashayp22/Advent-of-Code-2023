file1 = open('input1.txt', 'r')
Lines = file1.readlines()

grid = []

for line in Lines:
    if line[-1] == "\n":
        line = line[:-1]

    grid.append([r for r in line])

n = len(grid)
m = len(grid[0])

def print_ans_on_grid(grid, ans):
    for i in range(n):
        r = ""
        for j in range(m):
            if (i, j) in ans:
                r += "O"
            else:
                r += grid[i][j]
        print(r)


queue = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            queue.append((i, j, 0))
            grid[i][j] = "."

visited = set(queue)

ans = set()

while len(queue) > 0:
    i, j, dist = queue.pop(0)

    if dist == 64:
        ans.add((i, j))
    else:
        for new_i, new_j in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= new_i < n and 0 <= new_j < m and (new_i, new_j, dist+1) not in visited and grid[new_i][new_j] == ".":
                queue.append((new_i, new_j, dist+1))
                visited.add((new_i, new_j, dist+1))

print_ans_on_grid(grid, ans)
print(f"Answer: {len(ans)}")