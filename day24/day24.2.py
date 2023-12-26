from sympy import solve
from sympy.abc import x, y, z, a, b, c, u, v, t

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

hailstones = []

for line in Lines:
    if line[-1] == "\n":
        line = line[0:-1]

    split_line = line.split(" @ ")
    pos = split_line[0].split(", ")
    vel = split_line[1].split(", ")

    hailstones.append((int(pos[0]), int(pos[1]), int(pos[2]), int(vel[0]), int(vel[1]), int(vel[2])))

"""
Unknown variables: x, y, z, a, b, c, u, v, t
Where our stone is x, y, z @ a, b, c
S(t) = an equation representing our stones movement
h1(t) =  an equation representing the first hailstone movement
h2(t) =  an equation representing the second hailstone movement
h3(t) =  an equation representing the third hailstone movement

Three hailstones is enough to arrive at a unique answer

We want to solve for these 9 variables with 9 equations. Each equation below represents 3 equations since we must consider x, y, and z
S(u) = h1(u)
S(v) = h1(v)
S(t) = h1(t)
"""
first = hailstones[0]
second = hailstones[1]
third = hailstones[2]

S_equations = [x + a*u - (first[0] + first[3] * u),
               y + b*u - (first[1] + first[4] * u),
               z + c*u - (first[2] + first[5] * u),
               x + a*v - (second[0] + second[3] * v),
               y + b*v - (second[1] + second[4] * v),
               z + c*v - (second[2] + second[5] * v),
               x + a*t - (third[0] + third[3] * t),
               y + b*t - (third[1] + third[4] * t),
               z + c*t - (third[2] + third[5] * t)]

ans = solve(S_equations, [x, y, z, a, b, c, u, v, t], dict=True)[0]
ans = 349084334634500 + 252498326441926 + 121393830576314
print(f"Answer: {ans}")