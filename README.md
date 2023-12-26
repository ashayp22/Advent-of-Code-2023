# Advent of Code 2023

My Python solutions for [Advent of Code 2023](https://adventofcode.com/2023/). 
Solutions for each day are listed in the folder, and some days only contain the solution for Part Two. 

## Approaches

My goal is to find the correct answer within a reasonable amount of time (under 3 minutes).


- Day 1: String parsing
- Day 2: String parsing
- Day 3: Search input and check all 8 directions for part numbers
- Day 4: Linear time search, keeping track of duplicate cards
- Day 5: Backwards search from location to seed (took some time to run)
- Day 6: Checked all possible button hold times and solved a corresponding quadratic equation 
- Day 7: Main difficulty was creating a function to get the card's rank
- Day 8: Used Least Common Multiple
- Day 9: Iteration to calculate the sums on the sides of the triangle
- Day 10: Parsed into a graph, expanded the graph by a factor of 2, and did a flood fill
- Day 11: The shortest path between galaxies is always moving vertically, then horizontally
- Day 12: Dynamic programming with a recurrence and memoization
- Day 13: Tried matrix operations but failed, then found the reflection lines by checking all possible lines
- Day 14: Calculating the tilt row by row, and found the answer by finding a cycle after each tilt cycle  
- Day 15: Brute force calculate hash and update each box
- Day 16: BFS by not re-visiting a position and heading in the same direction as before
- Day 17: Graph transformation with layering and running Dijkstra's algorithm
- Day 18: Find the corner coordinates of the simple polygon and use the Shoelace formula
- Day 19: Generate all of the accepting ranges by backtracking from all of the accepting states
- Day 20: Evaluate each pulse in FIFO (queue) order and determine when each of gf's inputs (kr, zs, qk, kf) output HIGH, and then finding Least Common Multiple of those values. This is because kr, zs, qk, kf must output HIGH in order for gf to output LOW to rf.
- Day 21: Since the grid is a square and we expand from the center, the number of tiles covered grows quadratically for each factor of n, where n is the grid length. Hence, we can fit a quadratic function g from (0, f(65)), (1, f(65 + n)), (2, f(65 + 2*n)), and our final answer will be g(202300).
- Day 22: Originally tried to directly calculate which blocks supported which blocks using segment intersection, but that failed :( Switched to sorting bricks by minimum z-position and simulating each brick falling down 1 unit at a time until they collide with another brick.
- Day 23: Run modifed DFS by visiting the same node in different paths (but not allowing cycles in a path) to explore all paths, and collapsing nodes that have two neighbors
- Day 24: For part 1, check line intersection. For part 2, notice that we can arrive at a unique rock position/velocity with only 3 hailstones, and so we construct a system of 9 linear equations with 9 variables to solve for the rock's position.