max_lst=0
max_num=0
for i in range(5):
    n= list(map(int,input().split()))
    n= sum(n)
    if max_lst<n:
        max_lst = n
        max_num = i

print(max_num+1,max_lst)