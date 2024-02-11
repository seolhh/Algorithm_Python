import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
visited = [[False]*m for i in range(n)]
cnt = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(x,y):
    global cnt
    visited[x][y]=True

    if arr[x][y] =='P':
        cnt+=1

    for i in range(4):
        newX = x+dr[i]
        newY = y+dc[i]
        if 0<=newX<n and  0<=newY<m and visited[newX][newY] == False:
            if arr[newX][newY] !='X':
                dfs(newX,newY)


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            dfs(i,j)


if cnt == 0:
    print('TT')

else:
    print(cnt)
