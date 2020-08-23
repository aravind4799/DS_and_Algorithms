b=list(input())
a=list(input())

length1=len(strng1)
length2=len(strng2)

dp_matrix=[["" for i in range(length1+1)] for j in range(length2+1)]

for i in range(length1+1):
    for j in range(length2+1):
        if i==0 or j==0:
            dp_matrix[i][j]=0
        elif strng1[i-1]==strng2[j-1]:
            dp_matrix[i][j]=dp_matrix[i-1][j-1]+1
        else:
            dp_matrix[i][j]=max(dp_matrix[i-1][j],dp_matrix[i][j-1])

print(dp_matrix[length1][length2])



