a=list(map(int,input().split()))
j=1
l=len(a)
while(j<l):
    key=a[j]
    i=j-1
    while(i>=0 and key<a[i]):
        a[i+1]=a[i]
        i-=1
    a[i+1]=key
    print(a)
    j+=1
print(a)

    