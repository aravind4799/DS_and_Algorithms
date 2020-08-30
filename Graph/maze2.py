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

# 1 1 1 0
# 0 X 0 1
# 1 1 1 1
# 1 0 1 Y

# 1 X 0
# 0 1 1
# 0 1 Y

# maze=[[1,"X",0],[0,1,1],[0,1,"Y"]]
maze=[[1,1,1,0],[0,"X",0,1],[1,1,1,1],[1,0,1,"Y"]]
from queue import Queue
visited={}
parent={}
# maze=[[1,1,1,0,1,1,1],[1,"X",1,0,1,1,1],[1,0,1,1,1,0,1],[1,0,1,1,0,1,1],[1,1,0,1,1,1,1],
# [1,1,1,1,0,"Y",1],[0,0,1,1,0,1,0]]



def get_valid_adj(val,a):
    i,j=val
    l=len(a[0])
    h=len(a)

    if i+1<l and a[i+1][j]!=0:
        yield((i+1,j))
    if i-1>=0 and a[i-1][j]!=0:
        yield((i-1,j))
    if j+1<h and a[i][j+1]!=0:
        yield((i,j+1))
    if j-1>=0 and a[i][j-1]!=0:
        yield((i,j-1))


def dfs(start,maze,path=[]):
    stack=[start]
    while stack:
        print(stack)
        v=stack.pop()
        m,n=v
        if v in path:
            continue
        path.append(v)
        if maze[m][n]=='Y':
            return path
        for n in get_valid_adj(v,maze):
            stack.append(n)
    return []
def bfs(start,visited,parent,maze):
    bfs_path=[]
    path=[]
    q=Queue()
    q.put(start)
    visited[start]=True
    bfs_path.append(start)
    while not q.empty():
        v=q.get()
        i,j=v
        if maze[i][j]=='Y':
            end=(i,j)
            while end is not None:
                path.append((end))
                end=parent[end]
            return path[::-1],bfs_path
        for n in get_valid_adj(v,maze):
            if not visited[n]:
                visited[n]=True
                parent[n]=v
                bfs_path.append(n)
                q.put(n)
    return []

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j]=="X":
            start=(i,j)
            visited[(i,j)]=False
            parent[(i,j)]=None
            continue
        if maze[i][j]=="Y":
            end=(i,j)
            visited[(i,j)]=False
            parent[(i,j)]=None
            continue
        if maze[i][j]==1:
            visited[(i,j)]=False
            parent[(i,j)]=None


ans,bfs_path=bfs(start,visited,parent,maze)
# ans=dfs(start,maze)
# print(ans)
print(bfs_path)
if len(ans)==0:
    print("no path exists")

ans_matrix=[[0 for j in range(len(maze[0]))]for i in range(len(maze))]


for i in range(len(ans_matrix)):
    for j in range(len(ans_matrix[0])):
        if (i,j)==start:
            ans_matrix[i][j]='X'
            continue
        if (i,j)==end:
            ans_matrix[i][j]='Y'
            continue
        if (i,j) in ans:
            ans_matrix[i][j]=1

for i in range(len(ans_matrix)):
    for j in range(len(ans_matrix[0])):
        print(ans_matrix[i][j],end=" ")
    print()

        


