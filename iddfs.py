visited = []
path = []

parent = {}
graph = {'A':['B','C'],
         'B':['D','E'],
         'C':['F','G'],
         'D':[],
         'E':[],
         'F':[],
         'G':[]}

def findpath(goal):
  global parent, path
  while goal!='':
    path.append(goal)
    goal = parent[goal]

def DFS(current, goal, lim=float('inf'), depth=0):
  print("DFS called on node : ",current)
  global graph, parent, visited
  visited.append(current)
  if current == goal :
    findpath(goal)
    return 1
  if depth==lim:
    return
  for child in graph[current]:
    parent[child] = current
    if DFS(child, goal, lim, depth+1)==1:
      return 1

parent['A']=''
goal = input("Enter goal node : ")
maxdep = int(input("Enter max depth : "))
l=0
while path==[] and l<maxdep:
  print("With limit : ",l)
  DFS('A',goal,lim = l,depth = 0)
  l+=1
  print()

print()
if path==[]:
  print("Goal node not found")
else:
  path.reverse()
  BFSpath = '->'.join(path)
  print('Path : ',BFSpath)
  print("Found when depth was allowed upto ",l)
