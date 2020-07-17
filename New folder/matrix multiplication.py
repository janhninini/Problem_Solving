x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[3,2,1],
   [6,5,4],
   [9,8,7]]
z=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j] += x[i][k]*y[k][j]

for i in z:
    print(i)
