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

# Expand the universe
m = len(universe[0])
i = 0

empty_cols = set([i for i in range(m)])

while i < len(universe):
    for j in range(m):
        if universe[i][j] == "#" and j in empty_cols:
            empty_cols.remove(j)

    if universe[i] == "." * m:
        universe.insert(i, "." * m)
        i += 2
    else:
        i += 1

empty_cols = list(empty_cols)
print(empty_cols)

j = 0
ex = 0

while j < len(universe[0]):
    if j - ex in empty_cols:
        # Add empty column
        for i in range(len(universe)):
            universe[i] = universe[i][0:j+1] + "." + universe[i][j+1:]
        j += 2
        ex += 1
    else:
        j += 1

print_universe(universe)

# Run BFS to find shortest distance
n = len(universe)
m = len(universe[0])

galaxy = []

for i in range(n):
    for j in range(m):
        if universe[i][j] == "#":
            galaxy.append((i, j))

print(f"{n} x {m}")
print(len(galaxy))

dist = [[-float("inf") for _ in range(len(galaxy))] for _ in range(len(galaxy))]

def find_dist(start):
    queue = [(galaxy[start], 0)]
    visited = set()
    visited.add(start)

    while len(queue) > 0:
        (a, b), distance = queue.pop(0)

        if (a, b) in galaxy:
            idx = galaxy.index((a, b))
            dist[start][idx] = distance

        # Go over neighbors
        for c, d in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
            if 0 <= c < n and 0 <= d < m and (c, d) not in visited:
                queue.append(((c, d), distance + 1))
                visited.add((c, d))

for i in range(len(galaxy)):
    find_dist(i)
    print(f"Finish {i}")

sum = 0

pairs = 0

for i in range(len(galaxy)):
    for j in range(i+1, len(galaxy)):
        pairs += 1
        sum += dist[i][j]

print_universe(dist)

print(sum)
