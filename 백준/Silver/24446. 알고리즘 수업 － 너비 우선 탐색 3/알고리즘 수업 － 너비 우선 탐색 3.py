from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
G = [[] for i in range(n+1)]
visited = [-1] *(n+1)



def bfs(start):
    Q = deque()
    Q.append(start)

    visited[start] = 0


    while Q:
        v = Q.popleft()
        for i in G[v]:
            if visited[i] == -1:
                visited[i] =visited[v]+1
                Q.append(i)





for i in range(m):
    x,y = map(int,input().split())
    G[x].append(y)
    G[y].append(x)

bfs(r)


for i in visited[1:]:
    print(i)