# 케빈베이컨이 가장 작으려면 최단경로로 모두 돌아야 한다.

from collections import deque
n,m = map(int,input().split())
G = [[]for _ in range(n+1)]
result = [0]*(n+1)


def bfs(start):
    visited = [-1]*(n+1)
    Q = deque([start])
    visited[start] = 0

    while Q:
        v = Q.popleft()
        for x in G[v]:
            if visited[x] == -1:
                visited[x] = visited[v] +1
                Q.append(x)


    result[start]=sum(visited)

for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, n+1): #start 가 안정해져있고 계속 돌아야 함 5개.
    bfs(i)


print(result.index(min(result[1:])))


