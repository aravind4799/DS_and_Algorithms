# 8 11
# a b
# a c
# b c
# b g
# a e
# a d
# e d
# h d
# f h
# f e
# f g
# a

# 6 6
# a c
# a b
# c d
# b d
# d e
# e f
# a
n,e=map(int,input().split())
adj_dict={}
#for bfs we need visited array
visited={}

for i in range(e):
    x,y=input().split()
    if x not in adj_dict:
        adj_dict[x]=[y]
    else:
        adj_dict[x].append(y)
    if y not in adj_dict:
        adj_dict[y]=[x]
    else:
        adj_dict[y].append(x)
    
start = input()

for node in adj_dict:
    visited[node]=False

# using stack dfs search
# def dfs(adj_dict,start):
#     if start not in adj_dict:
#         return -1
#     stack,path=[start],[]
#     while stack:
#         vertex=stack.pop()
#         if vertex in path:
#             continue
#         path.append(vertex)
#         for n in adj_dict[vertex]:
#             stack.append(n)
#     return path

# using recursion
# def dfs(adj_dict,start,path=[]):
#     if start not in adj_dict:
#         return -1
#     path+=[start]
#     for n in adj_dict[start]:
#         if n not in path:
#             path=dfs(adj_dict,n,path)
#     return path

#bfs search

from queue import Queue

# def bfs(adj_dict,start):
#     q=Queue()
#     path=[]
#     q.put(start)
#     while not q.empty():
#         v = q.get()
#         visited[v]=True
#         path.append(v)
#         for n in adj_dict[v]:
#             if not visited[n]:
#                 q.put(n)           
#     return path

def bfs(adj,start):
    q=Queue()
    path=[]
    q.put(start)
    visited[start]=True
    while not q.empty():
        v = q.get()
        path.append(v)
        for n in adj[v]:
            if not visited[n]:
                visited[n]=True
                q.put(n)
    return path





      

path=bfs(adj_dict,start)
print(path)



        
