import networkx as nx

file1 = open('input.txt', 'r')
Lines = file1.readlines()

graph = nx.Graph()

for line in Lines:
    if line[-1] == "\n":
        line = line[0:-1]

    split_line = line.split(": ")
    u = split_line[0]
    neighbors = split_line[1].split(" ")

    for v in neighbors:
        graph.add_edge(u, v)

_, partition = nx.stoer_wagner(graph)
ans = len(partition[0]) * len(partition[1])

print(f"Answer: {ans}")