#day 2 assignment
#4

matrix=[[4,6,7,8],[3,7,2,7],[7,3,7,5]]
result=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix)):
      for j in range(len(matrix[0])):
          result[j][i]=matrix[i][j]
for res in result:
    print (res)
