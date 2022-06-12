MAX, MIN = 1000, -1000
def minimax(d, n, maximizingPlayer, values, a, b):
    if d == 3:
        return values[n]
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2): 
            val = minimax(d + 1, n * 2 + i,False, values, a, b)
            best = max(best, val)
            a = max(a, best)
            if b <= a:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(d + 1, n * 2 + i,True, values, a, b)
            best = min(best, val)
            b = min(b, best)
            if b <= a:
                break  
        return best
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1] 
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))
