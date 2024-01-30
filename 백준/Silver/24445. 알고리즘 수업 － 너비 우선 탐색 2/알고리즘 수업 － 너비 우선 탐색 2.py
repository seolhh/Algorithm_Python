from collections import deque
import sys

input = sys.stdin.readline

n,m,r = map(int,input().split())
G = [[] for i in range(n+1)]
visited = [0]*(n+1)


def bfs(start):
    Q = deque()
    Q.append(start)
    cnt =1
    visited[start] = cnt

    for i in range(n + 1):  # 내림차순으로 정렬
        G[i].sort(reverse=True)

    while Q:
        v = Q.popleft()
        for i in G[v]:
            if visited[i] ==0:
                Q.append(i)
                cnt+=1
                visited[i] = cnt
        #print("비지티드",visited)

for _ in range(m):
    x,y = map(int,input().split())
    G[x].append(y)
    G[y].append(x)



bfs(r)


for i in visited[1:]:
    print(i)

