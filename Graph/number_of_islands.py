



grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j]=int(grid[i][j])




def valid(grid,x,y):
    if 0<= x <len(grid) and 0<= y <len(grid[0]) and grid[x][y]!=0:
            return True
    return False
                
total=0
d={}
visited={}
#creating adj_list
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]==1:
            d[(i,j)]=[]
            visited[(i,j)]=False
            #down
            if(valid(grid,i-1,j)):
                d[(i,j)].append((i-1,j))
            #left
            if(valid(grid,i,j-1)):
                d[(i,j)].append((i,j-1))
            #up
            if(valid(grid,i+1,j)):
                d[(i,j)].append((i+1,j))
            #right
            if(valid(grid,i,j+1)):
                d[(i,j)].append((i,j+1))

#dfs
def dfs(grid,start):
    path,stack=[],[start]
    while stack:
        v = stack.pop()
        if v in path:
            continue
        path.append(v)
        visited[v]=True
        for n in d[v]:
            stack.append(n)
    return 1
    
    
    
           
                
        
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]==1 and visited[(i,j)]==False:
                total+=dfs(grid,(i,j))

print(total)