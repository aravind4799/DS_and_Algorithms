from time import time
#printing prime in given range
def is_prime(n):
    if n==1 or n==0:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def prime_range(x,y):
    start=time()
    ans=[]
    for i in range(x,y+1):
        if is_prime(i):
            ans.append(i)
    end=time()
    return ans,end-start

def seive(x,y):
    start=time()
    ans=[]
    if abs(x-y)-1==0:
        return None
    visited=[True]*(y-2)
    p=2
    while True:
        multipler=2
        multiple=p*multipler
        while(multiple<y):    
            visited[multiple-2]=False
            multipler+=1
            multiple=p*multipler
        for i,prime in enumerate(visited):
            if prime and i+2>p:
                p=i+2
                break
        else:
            break
    for i,prime in enumerate(visited):
        if prime and i+2>x:
            ans.append(i+2)
    end=time()
    return ans,end-start

ans,time=seive(1,100)
print(ans)
print(time)