class Puzzle:
    puzzlebox = [[]]
    size = ''
    steps = []
    goal = [[]]
    
    def __init__(self,size):
        self.size = size
        self.puzzlebox = [[0 for j in range(self.size)] for k in range(self.size)]
        self.boxinput()
        self.goal = [[j*self.size+k for k in range(1,self.size+1)] for j in range(self.size)]
        self.goal[-1][-1]=0
    
    def boxinput(self):
        print("Enter the value at : ")
        print("(Enter 0 at blank) ")
        for j in range(1,self.size+1):
            for k in range(1,self.size+1):
                self.puzzlebox[j-1][k-1] = int(input("Row "+str(j)+" Col "+str(k)+ " : "))
                if self.puzzlebox[j-1][k-1]==0:
                    self.blankpos = [j-1,k-1]        
    
    def evaluate(self):
        gn = 0
        laststate = ''
        for row in self.puzzlebox:
            print(row)
        print()
        while self.gethn(self.puzzlebox)!=0 and gn<10:
            x,y = self.blankpos[0],self.blankpos[1]
            moves = []
            if x+1<self.size: moves.append([x+1,y,'D'])
            if x-1>-1: moves.append([x-1,y,'U'])
            if y-1>-1: moves.append([x,y-1,'L'])
            if y+1<self.size: moves.append([x,y+1,'R'])
            rem = []
            for move in moves:
                if [move[0],move[1]]==laststate:
                    rem = move
            if rem!=[]:
                moves.remove(rem)
            fns = {}
            for mo in moves:
                fns[mo[-1]]=gn+self.gethn(self.move(mo))
            minfn = fns[moves[0][-1]]
            nextstate = ''
            for key in fns.keys():
                if fns[key]<=minfn:
                    minfn = fns[key]
                    nextstate = key
            self.steps.append(nextstate)
            laststate = self.blankpos
            if nextstate=='D': self.blankpos = [x+1,y]
            elif nextstate=='U': self.blankpos = [x-1,y]
            elif nextstate=='L': self.blankpos = [x,y-1]
            elif nextstate=='R': self.blankpos = [x,y+1]
            self.puzzlebox = self.move(laststate)
            gn+=1
            for row in self.puzzlebox:
                print(row)
            print("F(n) : ",minfn,"\n")

        print("Sequence of moves for blank are : ")
        dirs = {'R':'Right', 'L':'Left', 'U':'Up', 'D':'Down'}
        for step in self.steps:
            print(dirs[step])

    def gethn(self, boxstate):
        hn = 0
        for row in range(self.size):
            for col in range(self.size):
                if boxstate[row][col]!=self.goal[row][col]:
                    hn+=1
        return hn
        
    def move(self, mo):
        newbox = [[self.puzzlebox[j][k]  for k in range(self.size)] for j in range(self.size)]
        x = self.blankpos[0]
        y = self.blankpos[1]
        newbox[x][y], newbox[mo[0]][mo[1]] = newbox[mo[0]][mo[1]], newbox[x][y]
        return newbox

if __name__=="__main__":
    p = Puzzle(3)
    p.evaluate()