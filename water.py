jug1 = int(input('Enter jug1 capacity :'))
jug2 = int(input('Enter jug2 capacity :'))
aim  = int(input('Enter target capacity :'))
visited = {}

def WaterJugSolver(amt1, amt2):
  global visited
  if (amt1==aim and amt2==0) or (amt2==aim and amt1==0):
    print(amt1, amt2)
    return True
  if visited.get((amt1,amt2), False)==False:
    print(amt1, amt2)
    visited[(amt1,amt2)]=True
    return (
        WaterJugSolver(jug1, amt2) or
        WaterJugSolver(amt1, jug2) or
        WaterJugSolver(0, amt2) or
        WaterJugSolver(amt1, 0) or
        WaterJugSolver(amt1 + min(amt2, jug1-amt1), amt2 - min(amt2, jug1-amt1)) or
        WaterJugSolver(amt1 - min(amt1, jug2-amt2), amt2 + min(amt1, jug2-amt2))
    )
  else:
    return False

print("Steps  :")
WaterJugSolver(0,0)