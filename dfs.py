visited = []
def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=' ')
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F','G'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : []
}
dfs(visited, graph, 'A')