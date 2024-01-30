from collections import deque

n = int(input())
a,b = map(int,input().split())
m = int(input())

G = [[] for i in range(n+1)]
q = deque()
visited = [0]*(n+1)



def bfs(start):
    q.append(start)
    visited[start] = 1


    while q:
        v = q.popleft()


        for i in G[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v]+1




for _ in range(m):
    x,y = map(int,input().split())
    G[x].append(y)
    G[y].append(x)
# print(G)


bfs(a)

if visited[b] != 0:
    print(visited[b] -1)  # 시작 노드를 0촌으로 카운트하므로 수정합니다.
else:
    print(-1)