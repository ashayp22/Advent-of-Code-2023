file1 = open('input1.txt', 'r')
Lines = file1.readlines()

grid = []

for line in Lines:
    if line[-1] == "\n":
        line = line[:-1]

    grid.append([r for r in line])

n = len(grid)
m = len(grid[0])

print(f"{n}, {m}")

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

    if dist == 131:
        ans.add((i, j))
    else:
        for new_i, new_j in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if (new_i, new_j, dist+1) not in visited and grid[new_i % n][new_j % m] == ".":
                queue.append((new_i, new_j, dist+1))
                visited.add((new_i, new_j, dist+1))


"""
Since the grid is a square and we expand from the center, the number of tiles covered grows quadratically for each factor of n, 
where n is the grid length. 

The intuition for this comes from the fact that if we represent the entire grid by a single tile, and take 1 step, we cover 4 tiles.
After 2 steps, we cover 9 tiles. After 3 steps, we cover 16 tiles, and so on....

With n = 131, we can fit a quadratic function g from (0, f(65)), (1, f(65 + n)), (2, f(65 + 2*n)), and our final answer will be g(202300) 
since 202300 * 131 + 65 = 26501365.
"""


# Check 65 -> 3868
# Check 65 + 131 = 196 -> 34368
# Check 65 + 131 * 2 = 327 -> 95262

print(f"Answer: {len(ans)}")
# print_ans_on_grid(grid, ans)