# 2 number of test cases

# 5 number of links
# 1 2
# 2 4
# 1 3
# 1 7
# 7 5
# 7 6
# 4 start node
# 6 end node

# 1
# 6
# a c
# a b
# c d
# b d
# d e
# e f
# a
# f

# 7 number of links
# 1 4
# 1 2
# 1 3
# 1 5
# 3 6
# 6 7
# 7 8
# 7 start node 
# 4 end node

# output:
# 3 length of path
# 3

import queue

testcase = int(input())

for i in range(testcase):
    adj_list={}
    nos_of_links = int(input())
    for j in range(nos_of_links):
        x,y = input().split()
        if x not in adj_list:
            adj_list[x]=[y]
        else:
            adj_list[x].append(y)
        if y not in adj_list:
            adj_list[y]=[x]
        else:
            adj_list[y].append(x)
    
    q=queue.Queue()
    #q=queue.LifoQueue() for stack
    visited={}
    parent={}
    level={}
    bfs_traversal_list=[]

    for node in adj_list:
        visited[node]= False
        parent[node] = None
        level[node]  =  -1
    
    s=(input()) #source node

    if s not in adj_list:
        print("enter valid start node")
        break
    
    visited[s]=True
    level[s]= 0
    q.put(s)

    while not q.empty():
        u = q.get()
        bfs_traversal_list.append(u)
        for v in adj_list[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                level[v]=level[u]+1
                q.put(v) 
    
    #level dict to find distance 
    #parent dict to find the path

    end = (input())
    
    print("BFS traversal from given start node")
    print(bfs_traversal_list)

    print("distance from source to end node")
    print(level[end])

    print('path to given start node to end node')
    path=[]
    while(end is not None):
        path.append(end)
        end = parent[end]

    print(path[::-1])
        
    





    
        



