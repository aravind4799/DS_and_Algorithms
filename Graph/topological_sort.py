# is a graph traversal with a condition
# i.e in the traversal order if there exist a edge between u-v then u comes before v,
# so before traversal a node all nodes that paths to it must be traversed
# works on DAG-Directed Acyclic Graphs(does'nt)

attacked_by=[-1,8,6,0,7,3,8,9,-1,6]
# alien_species=[0,1,2,3,4,5,6,7,8,9]//basically index of element in attacked_by

#means alien_species 0 is attacked by None(-1)
#means alien_species 1 is attacked by 8
#means alien_species 2 is attacked by 6

# to find number of groups that can be formed such that no two species attack each other
# -1 means they dont have enemies

#forming directed graph from 
from collections import defaultdict
d=defaultdict(lambda:[])
visited={}
indegree=[0]*len(attacked_by)
for i,j in enumerate(attacked_by):
    if j ==-1:
        continue
    if j not in d:
        d[j]=[i]
        indegree[i]+=1
    else:
        d[j].append(i)
        indegree[i]+=1

for i in d:
    visited[i]=False

stack=[]
for i,j in enumerate(indegree):
    if j==0:
        stack.append(i)


while stack:
    v=stack.pop()
    print(v)
    for n in d[v]:
        stack.append(n)
        indegree[n]-=1
        if indegree[n]==0:
            stack.append(n)
    
    
    








