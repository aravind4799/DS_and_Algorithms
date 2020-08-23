a=[1,2,1,3,3]
b=[2,6,3,4,5]
#a,b corresponds to links in graph
p=[1,2,3,4,4,2]
# p => popularity of each node
u=[5,1,2]
v=[4,6,3]
#u,v tour taken
x=[1,2,3]
#x is popularity which needs to be added



d={}
visited={}
parent={}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]]=[b[i]]
    else:
        d[a[i]].append(b[i])
    if b[i] not in d:
        d[b[i]]=[a[i]]
    else:
        d[b[i]].append(a[i])
    

import queue

def bfs(d,start,end):
    q=queue.Queue()
    for i in d:
        visited[i]=False
        parent[i]=None
    path=[]
    q.put(start)
    visited[start]=True
    while not q.empty():
        v = q.get()
        if v == end:
            while(end is not None):
                path.append(end)
                end=parent[end]
            return path[::-1]
        for n in d[v]:
            if not visited[n]:
                visited[n]=True
                parent[n]=v
                q.put(n)
    return []

def jack_and_jill(d,p,u,v,x):

    for i in range(len(u)):
        print(u[i])
        print(v[i])
        path=bfs(d,u[i],v[i])
        print(path)
        for j in path:
            p[j-1]+=x[i]
         
    ans=sum(p[::2])-sum(p[1::2])
    print(ans)

jack_and_jill(d,p,u,v,x)

