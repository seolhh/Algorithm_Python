import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    h,w = map(int,input().split())
    arr = [list(input())for _ in range(h)]
    cnt = 0

    def dfs(x,y):
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for idx in range(4):
            newX = x + dr[idx]
            newY = y + dc[idx]

            if 0<= newX <h and 0<= newY <w and arr[newX][newY]=='#':
                arr[newX][newY] = '.'
                dfs(newX,newY)


    for i in range(h):
        for j in range(w):
            if arr[i][j] =='#':
                dfs(i,j)
                cnt+=1

    print(cnt)