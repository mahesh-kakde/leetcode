class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def sol():
    def cloneGraph(node):
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

    return cloneGraph

def build_graph(adjList):
    if not adjList:
        return None

    nodes = [Node(i + 1) for i in range(len(adjList))]

    for i, neighbors in enumerate(adjList):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor - 1])

    return nodes[0]

def get_adj_list(node):
    if not node:
        return []

    from collections import deque

    queue = deque([node])
    visited = {node.val}
    output = []

    while queue:
        curr = queue.popleft()
        output.append([neighbor.val for neighbor in curr.neighbors])

        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited.add(neighbor.val)
                queue.append(neighbor)

    return output

cloneGraph = sol()

adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
graph1 = build_graph(adjList1)
clone1 = cloneGraph(graph1)

adjList2 = [[]]
graph2 = build_graph(adjList2)
clone2 = cloneGraph(graph2)

adjList3 = []
graph3 = build_graph(adjList3)
clone3 = cloneGraph(graph3)

output = []
output.append(get_adj_list(clone1))
output.append(get_adj_list(clone2))
output.append(get_adj_list(clone3))

print(output)