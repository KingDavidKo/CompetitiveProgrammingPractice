import sys
y = int(input())
x = int(input())
sys.setrecursionlimit(4000000)
nodes = []
graph = {}
for i in range(y):
    nodes.append(list(map(int, input().split())))

for i in range(y):
    for j in range(x):
        if (i+1)*(j+1) in graph:
            graph[(i+1)*(j+1)].append(nodes[i][j])
        else:
            graph[(i+1)*(j+1)] = [nodes[i][j]]

visited = set()

def dfs(visited, graph, node, x, y):
    if node not in visited and node in graph:
        visited.add(node)
        if x*y in visited:
            return 0
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, x, y)

dfs(visited, graph, nodes[0][0], x, y)
if x*y in visited:
    print("yes")
else:
    print("no")