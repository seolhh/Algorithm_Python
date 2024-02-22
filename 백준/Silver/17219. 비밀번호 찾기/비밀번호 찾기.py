import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr={}
for _ in range(n):
    ad,pw = input().split()
    arr[ad] = pw
    # print(arr)

for _ in range(m):
    add = input().strip()
    print(arr[add])
