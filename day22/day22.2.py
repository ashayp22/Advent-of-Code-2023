file1 = open('input1.txt', 'r')
Lines = file1.readlines()

units = {}
bricks = []

class Unit:
    def __init__(self, brick, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.brick = brick

    def is_supported(self):
        if self.z == 1:
            return True
        elif (self.x, self.y, self.z - 1) in units:
            return units[(self.x, self.y, self.z - 1)].brick != self.brick
        return False

def fullrange(start, end):
    if start < end:
        return range(start, end+1)

    return range(end, start+1)

class Brick:
    def __init__(self, start, end):
        self.units = []
        for x in fullrange(start[0], end[0]):
            for y in fullrange(start[1], end[1]):
                for z in fullrange(start[2], end[2]):
                    unit = Unit(self, x, y, z)
                    self.units.append(unit)
                    units[(unit.x, unit.y, unit.z)] = unit

    def is_supported(self):
        supported = False
        for unit in self.units:
            if unit.is_supported():
                supported = True
        return supported

# Parse data
data = []

for line in Lines:
    if line[-1] == "\n":
        line = line[:-1]

    split = line.split("~")

    left = split[0].split(",")
    right = split[1].split(",")

    data.append(((int(left[0]), int(left[1]), int(left[2])), (int(right[0]), int(right[1]), int(right[2]))))

def fall_down(bricks):
    fallen_bricks = set()
    for brick in bricks:
        # print(brick)
        while not brick.is_supported():
            # Lower each unit
            for unit in brick.units:
                # We can move each unit down by one
                units[(unit.x, unit.y, unit.z - 1)] = unit
                units.pop((unit.x, unit.y, unit.z))
                unit.z -= 1
            fallen_bricks.add(brick)

    return len(fallen_bricks)

# Sort by min z value
n = len(data)
data = sorted(data, key=lambda b : min(b[0][2], b[1][2]))

# Create bricks and units
bricks = [Brick((b[0][0], b[0][1], b[0][2]), (b[1][0], b[1][1], b[1][2])) for b in data]

print(f"Bricks: {len(bricks)}")
print(f"Units: {len(units)}")

# Simulate falling down each unit
fall_down(bricks)

# To find the number of units to disintegrate, see if removing a unit
# and trying to fall the units again causes any units to fall
disintegrate = 0
total_fell = 0

for i in range(n):
    # Save a copy of the unit positions
    unit_copy = {pos: units[pos] for pos in units}

    # Delete the current brick's units
    for unit in bricks[i].units:
        del units[(unit.x, unit.y, unit.z)]

    new_bricks = bricks[0:i] + bricks[i+1:]
    fell = fall_down(new_bricks)
    total_fell += fell
    disintegrate += fell == 0

    # Reapply saved positions
    units = unit_copy

    for x, y, z in unit_copy:
        unit = unit_copy[(x, y, z)]
        unit.x = x
        unit.y = y
        unit.z = z
    
print(f"Part 1 Answer: {disintegrate}")
print(f"Part 2 Answer: {total_fell}")
