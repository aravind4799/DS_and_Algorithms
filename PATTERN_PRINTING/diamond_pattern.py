

n=int(input())
#n=3
#upper pyramid
for i in range(n):# i = 0,1,2
    for k in range(i+1,n):# loops: 2,1,0
        print(" ",end=" ")
    for j in range(2*(i+1)-1):#loops: 1,3,5
        print("*",end=" ")
    print()

#lower pyramid
for i in range(n-1,0,-1):
    for k in range(i,n):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()



