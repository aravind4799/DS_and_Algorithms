# 1 2 3
# 4 8 2
# 1 5 3

# ans:8
# minimum cost path: 1->2->2->3

# u are allowed to move down,diagonal,right

a=[[1,2,3],[4,8,2],[1,5,3]]
length=len(a)
col=len(a[0])
dp_matrix=[[0 for i in range(length)]for j in range(col)]

dp_matrix[0][0]=a[0][0]

#filling first row and column
for i in range(1,col):
    dp_matrix[i][0]= a[i][0]+dp_matrix[i-1][0]

for j in range(1,length):
    dp_matrix[0][j]=a[0][j]+dp_matrix[0][j-1]

#fill rest of the matrix

for i in range(1,length):
    for j in range(1,col):
        dp_matrix[i][j]=a[i][j]+min(dp_matrix[i-1][j],dp_matrix[i][j-1],dp_matrix[i-1][j-1])

print("ans:"+str(dp_matrix[length-1][col-1]))


