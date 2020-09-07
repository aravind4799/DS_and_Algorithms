#given a number find whether its prime

n= int(input("enter number to check"));
flag=0
for i in range(2,n):
    if n%i==0:
        print(i)
        flag=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")