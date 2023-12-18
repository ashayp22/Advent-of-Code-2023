file1 = open('input1.txt', 'r')
Lines = file1.readlines()

steps = []

# Parse input
for line in Lines:
    split_line = line.split(" ")

    color = split_line[2]

    if color[-1] == "\n":
        color = color[0:-1]

    steps.append((split_line[0], int(split_line[1]), color))

# Updates pos based on amount of steps and direction of move in
def applyDirection(pos, dir, amt):
    if dir == 3:
        return (pos[0], pos[1] - amt)
    elif dir == 2:
        return (pos[0] - amt, pos[1])
    elif dir == 1:
        return (pos[0], pos[1] + amt)
    return (pos[0] + amt, pos[1])

# Find direction and steps from the hexadecimal number
adjusted_steps = [(int(color[7]), int(color[2:7], 16)) for _, _, color in steps]

# Maps the direction to move in to complete a counterclockwise turn
# For example, if you move Right (0), then you must move Up (3) to make a counterclockwise turn
counterclockwise = {0: 3, 1: 0, 2: 1, 3: 2}

coors = [(0, 0)]
curr = (0, 0)
outside = 0
k = len(adjusted_steps)

for i in range(k):
    prev_i = (i-1) % k
    next_i = (i+1) % k
    direction, amount = adjusted_steps[i]

    """
    Assume that the polygon is drawn in a clockwise direction.
    To find the corners of the polygon, we adjust the polygon side length based on 
    whether the current corner and next corner are a part of a clockwise or counterclockwise turn
    
    - If both are clockwise, add 1 to the side length
    - If both are counterclockwise, subtract 1 from the side length
    - Else, do nothing
    
    This accounts for turning the # into valid corners for our polygon
    """

    next_direction, _ = adjusted_steps[next_i]
    prev_direction, _ = adjusted_steps[prev_i]

    is_prev_counterclockwise = counterclockwise[prev_direction] == direction
    is_next_counterclockwise = counterclockwise[direction] == next_direction

    extra = 0

    if is_prev_counterclockwise and is_next_counterclockwise:
        extra = -1
    elif not is_prev_counterclockwise and not is_next_counterclockwise:
        extra = 1

    # Calculate a corner of the polygon
    curr = applyDirection(curr, direction, amount + extra)
    coors.append(curr)

# Shoelace algorithm to the rescue using the corner coordinates we calculated above!
total = 0

for i in range(len(coors)-1):
    total += coors[i][0]*coors[i+1][1]
    total -= coors[i][1]*coors[i+1][0]

total = abs(total)//2

print(f"Answer: {total}")




