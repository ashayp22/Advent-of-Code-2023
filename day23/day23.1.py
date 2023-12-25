import sys

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

sys.setrecursionlimit(2000)

data = [line[:-1] if line[-1] == "\n" else line for line in Lines]

n = len(data)
m = len(data[0])

graph = {(i, j): [] for i in range(n) for j in range(m)}

def add_edge(i, j, dir):
    dir_map = {"L": (i, j-1), "R": (i, j+1), "U": (i-1, j), "D": (i+1, j)}
    a, b = dir_map[dir]

    if not (0 <= a < n and 0 <= b < m):
        return

    char = data[a][b]

    if char == "." \
            or (dir == "L" and char == "<") \
            or (dir == "R" and char == ">") \
            or (dir == "U" and char == "^") \
            or (dir == "D" and char == "v"):
        graph[(i, j)].append((a, b))

for i in range(n):
    for j in range(m):
        if data[i][j] == "<":
            add_edge(i, j, "L")
        elif data[i][j] == ">":
            add_edge(i, j, "R")
        elif data[i][j] == "^":
            add_edge(i, j, "U")
        elif data[i][j] == "v":
            add_edge(i, j, "D")
        elif data[i][j] == ".":
            add_edge(i, j, "L")
            add_edge(i, j, "R")
            add_edge(i, j, "U")
            add_edge(i, j, "D")

markings = [[0 for _ in range(m)] for _ in range(n)]

def is_cyclic(i, j, prev_i, prev_j):
    markings[i][j] = 1

    for new_i, new_j in graph[(i, j)]:
        if new_i == prev_i and new_j == prev_j:
            continue

        if markings[new_i][new_j] == 0 and is_cyclic(new_i, new_j, i, j):
            return True
        elif markings[new_i][new_j] == 1:
            return True

    markings[i][j] = 2
    return False


def detect_cycle():
    for i in range(n):
        for j in range(m):
            if markings[i][j] == 0 and is_cyclic(i, j, -1, -1):
                return True

    return False

def print_markings():
    for i in range(n):
        row = ""
        for j in range(m):
            if markings[i][j] != 0:
                row += "O"
            else:
                row += data[i][j]
        print(row)

# print(detect_cycle())
# print_markings()

visited = [[0 for _ in range(m)] for _ in range(n)]

def find_max_path(i, j):
    visited[i][j] = 1

    max_dist = 0

    for new_i, new_j in graph[(i, j)]:
        if visited[new_i][new_j] == 0:
            max_dist = max(max_dist, 1 + find_max_path(new_i, new_j))

    visited[i][j] = 0

    return max_dist

print(f"Answer: {find_max_path(0, 1)}")


