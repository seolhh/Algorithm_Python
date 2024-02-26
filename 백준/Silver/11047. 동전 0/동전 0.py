import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins=sorted((int(input()) for _ in range(n)),reverse=True)
# print(coins)
cnt = 0

for i in coins:
    cnt+=k//i
    k%=i



print(cnt)