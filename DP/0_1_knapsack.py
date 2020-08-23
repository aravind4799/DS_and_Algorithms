#        weight    value
# item1    5        60
# item2    3        50
# item3    4        70
# item4    2        30

# max_weight=5 find max value we can get!
# ans:80
# we choose item4 and item2


weight=[5,3,4,2]
max_weight=5
value=[60,50,70,30]
dp_matrix=[[None for j in range(max_weight+1)] for i in range(len(value))]

def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j],end=" ")
        print()

for i in range(len(dp_matrix)):
    for w in range(len(dp_matrix[0])):
        if i==0 or w==0:
            print("i==0 or j==0")
            dp_matrix[i][w]=0
            print_matrix(dp_matrix)
        elif weight[i]<= w:
            print ("{}<={}".format(value[i],w))
            dp_matrix[i][w]=max(dp_matrix[i-1][w],dp_matrix[i-1][w-weight[i]]+value[i])
            print_matrix(dp_matrix)
        else:
            print("else")
            dp_matrix[i][w]=dp_matrix[i-1][w]
            print_matrix(dp_matrix)

print("ans:"+str(dp_matrix[len(value)-1][max_weight]))
