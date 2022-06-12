class p:
   def inp1(self):
      x = [[0,0], [0,1], [1,0], [1,1]]
      return x
   def activation(self,y):
      w1 = 1
      w2 = 1
      z  = []
      for i in range(0,len(y)):
         q = w1*y[i][0] + w2*y[i][1]
         if q>=1:
            z.append(1)
         else:
            z.append(0)
      return z

a = p()
q = a.inp1()
b = a.activation(q)
print(b)