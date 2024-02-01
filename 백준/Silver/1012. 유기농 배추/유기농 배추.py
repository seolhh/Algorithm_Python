import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
for t in range(T):
    m,n,k = map(int,input().split())
    arr = [[0 for i in range(m+1)] for j in range(n+1)] #2차원배열 입력받기

    dirY = [-1, 1, 0, 0]
    dirX = [0, 0, -1, 1]


    def dfs(y, x):  # 상하좌우를 보는 함수
        for i in range(4):

            newY = y + dirY[i]
            newX = x + dirX[i]
            if 0 <= newY < n+1 and 0 <= newX < m+1 and arr[newY][newX] == 1:
                arr[newY][newX] = 0
                dfs(newY, newX)

    for i in range(k):
        x,y = map(int,input().split())
        arr[y+1][x+1] = 1 #배추의 위치를 1로 바꿔줌

    cnt = 0
    for i in range(m+1):
        for j in range(n+1):
            if arr[j][i] == 1:
                dfs(j,i)
                cnt+=1

    print(cnt)