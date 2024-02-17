
from collections import deque

N = int(input())   # 배열의 크기
arr = [list(map(int, input())) for _ in range(N)]   # 2차원배열 input 방법
# print(arr)

total = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            Q =deque()
            Q.append((i,j))
            cnt = 1
            arr[i][j] = 0

            while Q:
                r,c = Q.popleft()

                for idx in range(4):
                    nr = r + dr[idx]
                    nc = c + dc[idx]

                    if 0<=nr<N and 0<=nc<N and arr[nr][nc]==1:
                        cnt+=1
                        arr[nr][nc] = 0
                        Q.append((nr,nc))
            total.append(cnt)

print(len(total))

for i in sorted(total):
    print(i)