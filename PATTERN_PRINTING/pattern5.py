# odd pyramid
#    *
#   ***
#  *****
# *******

n=int(input())

for i in range(n):
    for k in range(i,n):
        print(" ",end=" ")
    for j in range(2*(i+1)-1):
        print("* ",end="")
    print()
