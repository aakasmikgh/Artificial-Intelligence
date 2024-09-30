def calcpathcost(path):
  pathcost=0
  for i in range (1,len(path)):
    edge=path[i-1]+path[i]
    stepcost=cost[edge]
    pathcost=pathcost+stepcost
  return pathcost
 
def BFS():
  expanded = []
  pathq=[start]
  fringe=[start]
  while fringe:
    node = fringe.pop(0)
    path=pathq.pop(0)
    if(node==goal):
      print("Goal found!!!!!")
      print("Solution Path:",path)
      pathcost=calcpathcost(path)
      print("Path Cost:",pathcost)
      break
    else:
      neighbours = graph[node]
      for n in neighbours:
        fringe.append(n)
        new_path=list(path)
        new_path.append(n)
        pathq.append(new_path)
    expanded.append(node)
graph={'a':['b','c'],'b':['c','d','e'],'c':['d','e'],'d':['g'],'e':['d','g']}
cost={'ab':5,'ac':2,'bc':6,'bd':2,'be':8,'cd':7,'ce':6,'dg':6,'ed':5,'eg':4}
start = 'a'
goal='g'
BFS()