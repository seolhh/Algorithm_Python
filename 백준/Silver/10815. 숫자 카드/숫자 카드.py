import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
m = int(input())

dic = {i:0 for i in list(map(int,input().split()))}

for i in lst:
    if i in dic:
        dic[i]+=1

print(*list(dic.values()))