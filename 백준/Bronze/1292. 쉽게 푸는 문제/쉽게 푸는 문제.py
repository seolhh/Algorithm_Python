N,M= map(int,input().split())
lst=[]
for i in range(1,M+1):
    if i>0:
        for j in range(i):
            if len(lst)==M:
                break
            else:
                lst.append(i)
lst=[0]+lst
print(sum(lst[N:M+1]))