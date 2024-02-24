n,m = map(int,input().split())
s=[]
t=[]
ans=[]
for _ in range(n):
    s.append(input())
for _ in range(m):
    t.append(input())
# print('t',t)
for i in t:
    # print(i,'i')
    if i in s:
        ans.append(i)
print(len(ans))