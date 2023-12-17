file1 = open('input1.txt', 'r')
Lines = file1.readlines()

weights = []

for line in Lines:
    if line[-1] == "\n":
        line = line[0:-1]

    weights.append([int(r) for r in line])

n = len(weights)
m = len(weights[0])

# Source: https://www.geeksforgeeks.org/shortest-path-in-a-directed-graph-by-dijkstras-algorithm/
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

infi = 100000000000

# Class of the node
class Node:

    # Adjacency list that shows the
    # vertexNumber of child vertex
    # and the weight of the edge
    def __init__(self, vertexNumber):
        self.vertexNumber = vertexNumber
        self.children = []

    # Function to add the child for
    # the given node
    def add_child(self, vNumber, length):
        p = Pair(vNumber, length)
        self.children.append(p)


# Function to find the distance of
# the node from the given source
# vertex to the destination vertex
def dijkstraDist(g, s, path):
    # Stores distance of each
    # vertex from source vertex
    dist = [infi for i in range(len(g))]

    # bool array that shows
    # whether the vertex 'i'
    # is visited or not
    visited = [False for i in range(len(g))]

    for i in range(len(g)):
        path[i] = -1
    dist[s] = 0
    path[s] = -1
    current = s

    # Set of vertices that has
    # a parent (one or more)
    # marked as visited
    sett = set()
    while (True):

        # Mark current as visited
        visited[current] = True
        for i in range(len(g[current].children)):
            v = g[current].children[i].first
            if (visited[v]):
                continue

            # Inserting into the
            # visited vertex
            sett.add(v)
            alt = dist[current] + g[current].children[i].second

            # Condition to check the distance
            # is correct and update it
            # if it is minimum from the previous
            # computed distance
            if (alt < dist[v]):
                dist[v] = alt
                path[v] = current
        if current in sett:
            sett.remove(current)
        if (len(sett) == 0):
            break

        # The new current
        minDist = infi
        index = 0

        # Loop to update the distance
        # of the vertices of the graph
        for a in sett:
            if (dist[a] < minDist):
                minDist = dist[a]
                index = a
        current = index
    return dist, path

idxToNodeName = {}

# Function to print the path
# from the source vertex to
# the destination vertex
def printPath(path, i, s):
    if (i != s):
        # Condition to check if
        # there is no path between
        # the vertices
        if (path[i] == -1):
            print("Path not found!!")
            return
        printPath(path, path[i], s)
        print(idxToNodeName[path[i]] + " ")

"""
Similar graph transformation as day17.1
"""
dir_to_mult = []

for i in range(1, 11):
    for j in ["N", "S", "W", "E"]:
        dir_to_mult.append(f"{i}-{j}")

dir_to_mult.append("END")

print(f"dir_to_mult: {len(dir_to_mult)}")

def getIdxFromVert(i, j, type):
    idx = dir_to_mult.index(type)
    return n*m*idx + m*i + j

for i in range(n):
    for j in range(m):
        for dir in dir_to_mult:
            idx = getIdxFromVert(i, j, dir)
            idxToNodeName[idx] = f"{i}, {j}, {dir}"

def moveInDirection(i, j, direction):
    mult = {"N": (-1, 0), "W": (0, -1), "S": (1, 0), "E": (0, 1)}
    mult_i, mult_j = mult[direction]
    return i + mult_i, j + mult_j

total_nodes = n*m*len(dir_to_mult)
print(f"{n} x {m} {total_nodes}")

vertices = [Node(i) for i in range(total_nodes)]

for i in range(n):
    for j in range(m):
        for type in dir_to_mult[0:-1]: # Skip the END state
            curr_idx = getIdxFromVert(i, j, type)

            can_move = []

            dash_idx = type.index("-")

            num_steps = int(type[0:dash_idx])
            direction = type[dash_idx+1:]

            left_right = {"N": ["N", "W", "E"], "S": ["S", "W", "E"], "W": ["W", "N", "S"], "E": ["E", "N", "S"]}

            for dir in left_right[direction]:
                if dir == direction and num_steps == 10:
                    # Stop moving in same direction
                    continue

                if dir != direction and num_steps < 4:
                    # Must move in the same direction
                    continue

                new_i, new_j = moveInDirection(i, j, dir)
                new_steps = num_steps + 1 if dir == direction else 1
                can_move.append((new_i, new_j, f"{new_steps}-{dir}"))

            # print(f"{i}, {j}, {type}: {can_move}")

            for new_i, new_j, new_type in can_move:
                if 0 <= new_i < n and 0 <= new_j < m:
                    new_idx = getIdxFromVert(new_i, new_j, new_type)

                    # Add directed edge
                    vertices[curr_idx].add_child(new_idx, weights[new_i][new_j])

# Connect each vertex to its END state with a 0 weighted edge
for i in range(n):
    for j in range(m):
        for dir in ["N", "S", "E", "W"]:
            for steps in range(4, 11):
                curr_idx = getIdxFromVert(i, j, f"{steps}-{dir}")
                end_idx = getIdxFromVert(i, j, "END")

                vertices[curr_idx].add_child(end_idx, 0)

# TODO: debug end state
start = getIdxFromVert(0, 0, "10-N")
print("Starting dijkstra")

path = [0 for i in range(total_nodes)]
dist, path = dijkstraDist(vertices, start, path)

final_end_idx = getIdxFromVert(n-1, m-1, "END")
min_dist = dist[final_end_idx]

# print(f"final_end_idx: {final_end_idx}")
print(f"Answer: {min_dist}")

# printPath(path, final_end_idx, start)

