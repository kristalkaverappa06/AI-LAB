from collections import deque

graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter neighbours separated by space: ").split()
    graph[node] = neighbours

start = input("Enter starting node: ")

visited = []
queue = deque()

visited.append(start)
queue.append(start)

print("BFS Traversal:")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)