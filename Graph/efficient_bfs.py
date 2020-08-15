from queue import Queue

def bfs(adj,start,end):
    q=Queue()
    visited = [False]*len(adj)
    q.put((start,0))
    while not q.empty():
        v,d = q.get()
        if v == end:
            return d
        visited[v]=True
        for n in adj[v]:
            if not visited[n]:
                q.put((n,d+1))
    return -1

n,m = map(int,input().split())

adj = [[] for i in range(n)]

for i in range(m):
    u,v = map(int,input.split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
start = int(intput())
end
            
