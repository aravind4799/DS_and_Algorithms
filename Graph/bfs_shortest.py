# 1
# 5 3
# 1 2
# 1 3
# 3 4
# 1

import math
import os
import random
import re
import sys
from queue import Queue
# Complete the bfs function below.
t=int(input())
nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
edges = []
for _ in range(m):
    edges.append(list(map(int, input().rstrip().split())))
s = int(input())

def bfs(n, m, edges, s):
    d=[[] for i in range(n) ]
    for i in range(len(edges)):
        u,v=edges[i]
        d[u-1].append(v)
        d[v-1].append(u)
    print(d)

    ans=[-1]*n
    visited=[False]*n
    q=Queue()
    q.put((s,0))
    visited[s-1]=True
    while not q.empty():
        v,dep=q.get()
        ans[v-1]=dep*6
        print(ans)
        for n in d[v-1]:
            if not visited[n-1]:
                visited[n-1]=True
                q.put((n,dep+1))
    ans.pop(s-1)
    return ans
print(bfs(n,m,edges,s))

    






