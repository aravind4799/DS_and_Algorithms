# inverse odd pyramid

# *******
#  *****
#   ***
#    *
# for n=4

n = int(input())

odd_lst=[]
for i in range(n):
    odd_lst.append(2*(i+1)-1)
odd_lst=sorted(odd_lst,reverse=True)


for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(odd_lst[i]):
        print("*",end=" ")
    print()