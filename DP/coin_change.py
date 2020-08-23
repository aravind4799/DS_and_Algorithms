amount=5
coins=[1,2,5]

# to find distinct combinations to make amount=5 using 1,2,5 coins
# ans=4

# 1,1,1,1,1
# 1,1,1,2
# 5
# 2,2,1

dp_matrix=[[None for i in range(amount+1)] for j in range(len(coins)+1)]

def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j],end=" ")
        print()

for i in range(len(dp_matrix)):
    for j in range(len(dp_matrix[0])):
        if i==0 and j==0:
            print("i==0 and j==0")
            dp_matrix[i][j]=1
            print(i,end=" ")
            print(j,end=" ")
            print()
            print_matrix(dp_matrix)
        elif i==0:
            print("i==0")
            print(i,end=" ")
            print(j,end=" ")
            print()
            dp_matrix[i][j]=0
            print_matrix(dp_matrix)
        elif j==0:
            print("j==0")
            print(i,end=" ")
            print(j,end=" ")
            print()
            dp_matrix[i][j]=1
            print_matrix(dp_matrix)       
        else:
            if(j-coins[i-1]>=0):
                print(i,end=" ")
                print(j,end=" ")
                print()
                dp_matrix[i][j]=dp_matrix[i-1][j]+dp_matrix[i][j-coins[i-1]]
                print_matrix(dp_matrix)
            else:
                print(i,end=" ")
                print(j,end=" ")
                print()
                dp_matrix[i][j]=dp_matrix[i-1][j]
                print_matrix(dp_matrix)
print()
print()
print("ans:"+str(dp_matrix[len(coins)][amount]))


