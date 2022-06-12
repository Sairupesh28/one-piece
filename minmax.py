def prntbox(s):
    print(s[:3])
    print(s[3:6])
    print(s[6:9])

def evalu(s):
    X = 0
    O = 0

    if 'O' not in s[:3]: X+=1
    if 'O' not in s[3:6]: X+=1
    if 'O' not in s[6:9]: X+=1
    if 'O' not in [s[0],s[3],s[6]] : X+=1
    if 'O' not in [s[1],s[4],s[7]] : X+=1
    if 'O' not in [s[2],s[5],s[8]] : X+=1
    if 'O' not in [s[0],s[4],s[8]] : X+=1
    if 'O' not in [s[2],s[4],s[6]] : X+=1

    if 'X' not in s[:3]: O+=1
    if 'X' not in s[3:6]: O+=1
    if 'X' not in s[6:9]: O+=1
    if 'X' not in [s[0],s[3],s[6]] : O+=1
    if 'X' not in [s[1],s[4],s[7]] : O+=1
    if 'X' not in [s[2],s[5],s[8]] : O+=1
    if 'X' not in [s[0],s[4],s[8]] : O+=1
    if 'X' not in [s[2],s[4],s[6]] : O+=1
    return X-O

def checkwin(s):
    rows = [[0,1,2],[3,4,5],[6,7,8]]
    cols = [[0,3,6],[1,4,7],[2,5,8]]
    diag = [[0,4,8],[2,4,6]]
    for r in rows:
        if s[r[0]]==s[r[1]] and s[r[1]]==s[r[2]]:
            if s[r[0]]=='X':
                print('Max player won')
                return 1
            elif s[r[0]]=='O':
                print("Min player won")
                return 1
    for r in cols:
        if s[r[0]]==s[r[1]] and s[r[1]]==s[r[2]]:
            if s[r[0]]=='X':
                print('Max player won')
                return 1
            elif s[r[0]]=='O':
                print("Min player won")
                return 1
    for r in diag:
        if s[r[0]]==s[r[1]] and s[r[1]]==s[r[2]]:
            if s[r[0]]=='X':
                print('Max player won')
                return 1
            elif s[r[0]]=='O':
                print("Min player won")
                return 1
    return -1

p = 1
s = ('_','_','X','O','_','O','_','X','_')

print("Initial state :")
prntbox(s)
print()

while '_' in s:
    d = {}
    if p==1:
        for pl in range(9):
            if s[pl] == '_':
                newb = list(s).copy()
                newb[pl] = 'X'
                d[tuple(newb)] = evalu(newb)
        nxt = ()
        score = -float('inf')
        for k in d.keys():
            if d[k]>score:
                nxt = k
                score = d[k]
        print("Max made move :")
        prntbox(nxt)
        print(d[nxt])
        print()
        s = nxt
    if p==-1:
        for pl in range(9):
            if s[pl] == '_':
                newb = list(s).copy()
                newb[pl] = 'O'
                d[tuple(newb)] = evalu(newb)
        score = float('inf')
        for k in d.keys():
            if d[k]<score:
                nxt = k
                score = d[k]
        print("Min made move :")
        prntbox(nxt)
        print(d[nxt])
        print()
        s = nxt
    if checkwin(s)==1:
        prntbox(s)
        break
    p*=-1
