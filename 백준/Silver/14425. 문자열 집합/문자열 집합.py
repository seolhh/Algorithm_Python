n,m = map(int,input().split())
cnt = 0
s = {input() for _ in range(n)}
for _ in range(m):
    if input() in s:
        cnt+=1

print(cnt)