from collections import deque
import sys
input= sys.stdin.readline

n,m,r = map(int,input().split())
G = [[] for i in range(n+1)]
visited = [-1]*(n+1)
depth = [0]*(n+1)

def bfs(start):
    Q = deque()
    Q.append(start)
    cnt = 1
    visited[start] = 0
    depth[start] = cnt
    while Q:
        v = Q.popleft()

        for i in G[v]:
            if visited[i] == -1:
                Q.append(i)
                visited[i] = visited[v]+1
                cnt+=1
                depth[i] = cnt
    # print(visited)
    # print(depth)


for _ in range(m):
    x,y = map(int,input().split())
    G[x].append(y)
    G[y].append(x)


bfs(r)

Sum = 0

for i in range(1,n+1):
    ab=visited[i]*depth[i]
    Sum+=ab


print(Sum)