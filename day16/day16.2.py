file1 = open('input1.txt', 'r')
Lines = file1.readlines()

grid = []
for line in Lines:
    row = [c for c in line]
    if row[-1] == "\n":
        row.pop()

    grid.append(row)

    n = len(grid)
    m = len(grid[0])

def move_in_direction(r, c, direction):
    if direction == "N":
        return r-1, c
    elif direction == "W":
        return r, c-1
    elif direction == "E":
        return r, c+1
    return r+1, c

def check_bounds(r, c):
    return 0 <= r < n and 0 <= c < m

def get_energized_tiles(start_r, start_c, start_direction):
    energized_tiles = set()
    visited = set()

    queue = [(start_r, start_c, start_direction)]

    energized_tiles.add((start_r, start_c))
    visited.add((start_r, start_c, start_direction))

    while len(queue) > 0:
        r, c, direction = queue.pop(0)

        new_moves = []

        # Which direction to go?
        if grid[r][c] == ".":
            # Keep moving in direction
            new_r, new_c = move_in_direction(r, c, direction)
            new_moves.append((new_r, new_c, direction))
        elif grid[r][c] == "-":
            if direction == "E" or direction == "W":
                # Keep moving in direction
                new_r, new_c = move_in_direction(r, c, direction)
                new_moves.append((new_r, new_c, direction))
            else:
                # Split the beam
                new_moves.append((r, c-1, "W"))
                new_moves.append((r, c+1, "E"))
        elif grid[r][c] == "|":
            if direction == "N" or direction == "S":
                # Keep moving in direction
                new_r, new_c = move_in_direction(r, c, direction)
                new_moves.append((new_r, new_c, direction))
            else:
                # Split the beam
                new_moves.append((r-1, c, "N"))
                new_moves.append((r+1, c, "S"))
        elif grid[r][c] == "\\":
            mirror = {"E": "S", "S": "E", "W": "N", "N": "W"}
            new_r, new_c = move_in_direction(r, c, mirror[direction])
            new_moves.append((new_r, new_c, mirror[direction]))
        elif grid[r][c] == "/":
            mirror = {"N": "E", "E": "N", "S": "W", "W": "S"}
            new_r, new_c = move_in_direction(r, c, mirror[direction])
            new_moves.append((new_r, new_c, mirror[direction]))

        for new_r, new_c, new_direction in new_moves:
            if check_bounds(new_r, new_c) and (new_r, new_c, new_direction) not in visited:
                queue.append((new_r, new_c, new_direction))
                visited.add((new_r, new_c, new_direction))
                energized_tiles.add((new_r, new_c))

    return len(energized_tiles)

max_ans = 0

start = []

for i in range(n):
    start.append((i, 0, "E"))
    start.append((i, m-1, "W"))

for j in range(m):
    start.append((0, j, "S"))
    start.append((n-1, j, "N"))

for start_r, start_c, start_direction in start:
    max_ans = max(max_ans, get_energized_tiles(start_r, start_c, start_direction))

print(f"Answer: {max_ans}")