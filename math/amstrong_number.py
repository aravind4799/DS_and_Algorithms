#check if given number is amstrong number
# if cube of individual digits sum up to given number then its amstrong number
n=int(input("enter number:"))
copy=n
total=0
while(copy>0):
    digit=copy%10
    total+=pow(digit,3)
    copy=copy//10
if total==n:
    print("amstrong")
else:
    print("not amstrong")