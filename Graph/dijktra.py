#minpathsum

# 31 100 65 12 18
# 10 13 47 157 6
# 100 113 174 11 33
# 88 124 41 20 140
# 99 32 111 41 20

# ans: 327

from collections import defaultdict
from queue import PriorityQueue

n=int(input())

a=[]

for i in range(n):
    a.append(list(map(int,input().split())))

d=defaultdict(lambda: 10**5)
q=PriorityQueue()

def getneigh(i,j,n):
    if i-1>=0:
        yield((i-1,j))
    if j-1>=0:
        yield((i,j-1))
    if i+1<n:
        yield((i+1,j))
    if j+1<n:
        yield((i,j+1))

d[(0,0)]=a[0][0]
q.put((d[0,0],0,0))

while not q.empty():
    dist,x,y=q.get()
    for i,j in getneigh(x,y,n):
        if d[(x,y)]+a[i][j]<d[(i,j)]:
            d[(i,j)]=d[(x,y)]+a[i][j]
            q.put((d[(i,j)],i,j))

print(d[(n-1,n-1)])



