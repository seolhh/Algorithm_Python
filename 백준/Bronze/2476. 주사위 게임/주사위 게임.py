
n=int(input())
list_all=[]
for i in range(n):
    n_lst=sorted(list(map(int,input().split())))
    if n_lst[0]==n_lst[1]==n_lst[2]:
        list_all.append(10000+(n_lst[0])*1000)
    elif n_lst[0]!=n_lst[1]!=n_lst[2]:
        list_all.append((n_lst[-1])*100)
    else:
        list_all.append(1000+(n_lst[1])*100)
print(max(list_all))