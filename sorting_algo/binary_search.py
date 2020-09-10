#binary search requires a sorted array

a=list(map(int,input().split()))
n=int(input())
a=sorted(a)
def binary_search(a,n):
    if len(a)==0 or len(a)==1 and a[0]!=n:
        return False
    
    mid=len(a)//2
    if a[mid]==n:
        return True
    elif a[mid]>n:
        return binary_search(a[:mid],n)
    else:
        return binary_search(a[mid+1:],n)
print(binary_search(a,n))       
