from collections import defaultdict
from queue import PriorityQueue

n = int(input())

a = []

for i in range(n):
    a.append(list(map(int,input().split())))

def getneigh(i,j,n):
    if i-1>=0:
        yield (i-1,j)
    if j-1>=0:
        yield (i,j-1)
    if i+1<n:
        yield (i+1,j)
    if j+1<n:
        yield (i,j+1)


dist = defaultdict(lambda : 10**5)
dist[(0,0)] = a[0][0]
q = PriorityQueue()
q.put((dist[(0,0)],0,0))


while not q.empty():
    d,x,y = q.get()
    for i,j in getneigh(x,y,n):
        if dist[(x,y)] + a[i][j] < dist[(i,j)]:
            dist[(i,j)] = dist[(x,y)] + a[i][j]
            q.put((dist[(i,j)],i,j))

print(dist[(n-1,n-1)])