import sys
input = sys.stdin.readline

from collections import deque
Q = deque()

n,m = map(int,input().split())
G = [[]for i in range(n+1)]
visited = [0]*(n+1)
cnt = 0

def bfs(start):
    global cnt

    visited[start] = 1
    Q.append(start)

    while Q:
         v = Q.popleft()
         for i in G[v]:
             if visited[i] == 0:
                visited[i] = 1
                Q.append(i)
    cnt+=1


for _ in range(m):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)


print(cnt)