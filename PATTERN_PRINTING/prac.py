# 1
# 3*2
# 4*5*6
# 10*9*8*7
# 11*12*13*14*15


#    *
#   ***
#  *****
#   ***
#    *
num=1
n=int(input())
#print upper triangle odd pyramid
for i in range(n):
    for k in range(i,n):
        print(" ",end=" ")
    for j in range(num):
        print("*",end=" ")
    print()
    num+=2
num-=4
#print lower triangle
for i in range(n-1):
    print("   ",end=" ")
    for k in range(i):
        print(" ",end=" ")
    for j in range(num):
        print("*",end=" ")
    print()
    num-=2

    

