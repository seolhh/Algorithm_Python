from collections import deque
import sys
input = sys.stdin.readline

# 총 필요한 그룹
# G = 접점괸계를 알 수 있는 그래프
# visited = 방문한 점에 대한 표시 리스트
# q = bfs를 하기 위해 탐색하기 위한 리스트


n,m,r = map(int,input().split())
G =[[] for _ in range(n+1)] # 그래프는 어떤 점이 어디를 방문했는지 한눈에 볼 수 있음
visited = [0]*(n+1)



def bfs(start):
    q = deque()
    q.append(start)

    cnt = 1
    visited[start] = 1

    while q:
        v = q.popleft()


        for i in G[v]:
            if visited[i] == 0:
                q.append(i)
                cnt+=1
                visited[i] = cnt



# for i in visited(1,n+1):
#     print(i)


for _ in range(m):
    a, b = map(int,input().split())
    G[a].append(b) # 양방향에 대비한 append
    G[b].append(a)


for i in range(n+1): # 그래프를 오름차순으로 정렬(작은 수 부터 탐색하기 위해)
    G[i].sort()


bfs(r)

for i in visited[1:]:
    print(i)






