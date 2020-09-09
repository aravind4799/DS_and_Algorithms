# given a string,
# reverse it and find which chars remains in same position as original

# n=str(input("enter a string:"))
# count=0

# for i in range(len(n)):
#     if n[i]==n[::-1][i]:
#         count+=1
# print(count)

#reverse a number


n=int(input("enter a number:"))
l=len(str(n))
ans=0
while(n!=0 and l>0):
    digit=n%10
    ans+=digit*pow(10,l-1)
    n=n//10
    l-=1
print(ans)
