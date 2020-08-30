# 1 = path
# 0 = wall
# X = Start
# Y = End
# need to find if there is a path from X to Y

# 1 1 1 0 1 1 1
# 1 X 1 0 1 1 1
# 1 0 1 1 1 0 1
# 1 0 1 1 0 1 1
# 1 1 0 1 1 1 1
# 1 1 1 1 0 Y 1
# 0 0 1 1 0 1 0

# 1 X 0
# 0 1 1
# 0 1 Y
maze=[[1,1,1,0],[0,"X",0,1],[1,1,1,1],[1,0,1,"Y"]]
# maze=[[1,"X",0],[0,1,1],[0,1,"Y"]]
from queue import Queue
# maze=[[1,1,1,0,1,1,1],[1,"X",1,0,1,1,1],[1,0,1,1,1,0,1],[1,0,1,1,0,1,1],[1,1,0,1,1,1,1],
# [1,1,1,1,0,"Y",1],[0,0,1,1,0,1,0]]


adj_dict={}
visited={}
parent={}

for i in range(len(maze)):
    for j in range(len(maze[i])):

        if maze[i][j]==1:
            adj_dict[(i,j)]=[]
            visited[(i,j)]=False
            parent[(i,j)]=None

        elif maze[i][j]=="Y":
            end=(i,j)
            adj_dict[(i,j)]=[]
            visited[(i,j)]=False
            parent[(i,j)]=None

        elif maze[i][j]=="X":
            start=(i,j)
            adj_dict[(i,j)]=[]
            visited[(i,j)]=False
            parent[(i,j)]=None

def valid_move(maze,x,y):
    if 0<=x<=len(maze)-1 and 0<=y<=len(maze[0])-1 and maze[x][y]!=0:
        return True
    return False


for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j]== 1 or maze[i][j]=="X" or maze[i][j]=="Y":

            if(valid_move(maze,i,j-1)):
                adj_dict[(i,j)].append((i,j-1))

            if(valid_move(maze,i+1,j)):
                adj_dict[(i,j)].append((i+1,j))

            if(valid_move(maze,i,j+1)):
                adj_dict[(i,j)].append((i,j+1))

            if(valid_move(maze,i-1,j)):
                adj_dict[(i,j)].append((i-1,j))
print(adj_dict)

# adj_dict={(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (1, 1), (0, 2)], (0, 2): [(0, 1), (1, 2)], (0, 4): [(1, 4), (0, 5)], (0, 5): [(0, 4), (1, 5), (0, 6)], (0, 6): [(0, 5), (1, 6)], (1, 0): [(2, 0), (1, 1), (0, 0)], (1, 1): [(0, 1),(1, 0),(1,2)], (1, 2): [(1, 1), (2, 2), (0, 2)], (1, 4): [(2, 4), (1, 5), (0, 4)], (1, 5): [(1, 4), (1, 6), (0, 5)], (1, 6): [(1, 5), (2, 6), (0, 6)], (2, 0): [(3, 0), (1, 0)], (2, 2): [(3, 2), (2, 3), (1, 2)], (2, 3): [(2, 2), (3, 3), (2, 4)], (2, 4): [(2, 3), (1, 4)], (2, 6): [(3, 6), (1, 6)], (3, 0): [(4, 0), (2, 0)], (3, 2): [(3, 3), (2, 2)], (3, 3): [(3, 2), (4, 3), (2, 3)], (3, 5): [(4, 5), (3, 6)], (3, 6): [(3, 5), (4, 6), (2, 6)], (4, 0): [(5, 0), (4, 1), (3, 0)], (4, 1): [(4, 0), (5, 1)], (4, 3): [(5, 3), (4, 4), (3, 3)], (4, 4): [(4, 3), (4, 5)], (4, 5): [(4, 4), (5, 5), (4, 6), (3, 5)], (4, 6): [(4, 5), (5, 6), (3, 6)], (5, 0): [(5, 1), (4, 0)], (5, 1): [(5, 0), (5, 2), (4, 1)], (5, 2): [(5, 1), (6, 2), (5, 3)], (5, 3): [(5, 2), (6, 3), (4, 3)], (5, 5): [(6, 5), (5, 6), (4, 5)], (5, 6): [(5, 5), (4, 6)], (6, 2): [(6, 3), (5, 2)], (6, 3): [(6, 2), (5, 3)], (6, 5): [(5, 5)]}

#use dfs to find a feasible solution
def dfs(adj_dict,start,end):
    stack,path=[start],[]
    while stack:
        print(stack)
        v = stack.pop()
        if v in path:
            continue
        path.append(v)
        if v==end:
            return path
        for n in adj_dict[v]:
            stack.append(n)
    return []

#use bfs to find the optimal or shortest path
def bfs(adj_dict,start,end):
    q=Queue()
    path=[]
    q.put(start)
    visited[start]=True
    while not q.empty():
        v = q.get()
        if v==end:
            while(end is not None):
                path.append(end)
                end=parent[end]
            return path[::-1]
            
        for n in adj_dict[v]:
            if not visited[n]:
                visited[n]=True
                parent[n]=v
                q.put(n)
    return []


path=bfs(adj_dict,start,end)
print(path)
if path:
    print("solution matrix:\n")
    sol=[[0 for j in range(len(maze[0]))] for i in range(len(maze))]
    for i,index in enumerate(path):
        x,y=index
        if i==0:
            sol[x][y]='X'
        elif i==len(path)-1:
            sol[x][y]='Y'
        else:
            sol[x][y]=1
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            print(sol[i][j],end=" ")
        print()
else:
    print("no valid path found")
            
            



    
   
    


    






