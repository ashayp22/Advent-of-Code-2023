file1 = open('input1.txt', 'r')
Lines = file1.readlines()

data = [line[:-1] if line[-1] == "\n" else line for line in Lines]

n = len(data)
m = len(data[0])

graph = {(i, j): [] for i in range(n) for j in range(m)}

# Construct the graph
def add_edge(i, j, dir):
    dir_map = {"L": (i, j-1), "R": (i, j+1), "U": (i-1, j), "D": (i+1, j)}
    a, b = dir_map[dir]

    if not (0 <= a < n and 0 <= b < m):
        return

    if data[a][b] != "#":
        graph[(i, j)].append((a, b))

for i in range(n):
    for j in range(m):
        if data[i][j] != "#":
            add_edge(i, j, "L")
            add_edge(i, j, "R")
            add_edge(i, j, "U")
            add_edge(i, j, "D")

def collapse_nodes(parent, child, dist=1):
    # Find the true children of this parent after collapsing child
    while len(graph[child]) == 2:
        # Find the next child
        parent_idx = graph[child].index(parent)
        parent = child
        child = graph[child][1-parent_idx]
        dist += 1
    return child, dist

# Update the graph based on collapsing nodes
graph = {p: [collapse_nodes(p, q) for q in graph[p]] for p in graph}

# Do a DFS search
visited = set()

def search(i, j):
    if (i, j) == (n - 1, m - 2):
        return 0

    # Keep track of the best value if we come across a node in the path
    visited.add((i, j))
    best = -float("inf")

    for (new_i, new_j), weight in graph[(i, j)]:
        if (new_i, new_j) not in visited:
            best = max(best, weight + search(new_i, new_j))

    visited.remove((i, j))
    return best

ans = search(0, 1)

print(f"Answer: {ans}")


