
n,k = map(int,input().split())
cnt = 0

lst = list(i for i in range(2,n+1))
while lst:
    min = lst[0]
    for i in lst[:]:
        if i%min==0:
            lst.remove(i)
            cnt+=1
            # print('cnt',cnt)
            if cnt == k:
                print(i)
                break
