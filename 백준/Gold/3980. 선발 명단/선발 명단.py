def dfs(n,sm):  # n은 선수 , sm은 모든 포지션 능력치 최대 합
    global Max
    if n==11:
        Max= max(sm,Max)
        return

    for j in range(11): # 포지션
        if V[j]==1:
            continue
        if arr[n][j]==0:
            continue
        V[j]=1
        dfs(n+1, sm+arr[n][j])
        V[j]=0

T = int(input())
for tc in range(T):
    arr = [list(map(int,input().split())) for _ in range(11)]
    V = [0]*11   # 포지션
    Max = 0 # 능력치의 합 최대값 변수

    dfs(0,0)
    print(Max)