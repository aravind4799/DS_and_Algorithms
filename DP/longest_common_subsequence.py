a=input("enter string1 :")
b=input("enter string2 :")

def lcs(x,y):
    len_x=len(x)
    len_y=len(y)
    matrix=[["" for i in range(len_x+1)] for j in range(len_y+1)]

    for i in range(len_x+1):
        for j in range(len_y+1):
            if i==0 or j==0:
                matrix[i][j]=0
            elif x[i-1]==y[j-1]:
                matrix[i][j]=matrix[i-1][j-1]+1
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
    return matrix[len_x][len_y]

a=lcs(a,b)
print(a)



