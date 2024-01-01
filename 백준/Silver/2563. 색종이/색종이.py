N = int(input())

cnt = 0
arr = [[0] *100 for _ in range(100)]
for n in range(N):
    c,r = map(int,input().split())

    for i in range(r,r+10):
        for j in range(c,c+10):
            if arr[i][j]==0:
                arr[i][j]+=1
                cnt+=1
            else:
                pass

print(cnt)