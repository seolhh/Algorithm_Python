n = int(input())

for _ in range(n):
    stack = []
    cnt=0
    a=list(input())
    for i in a:
        if i =='(':
            stack.append(i)
        else:
            if len(stack)!=0:
                stack.pop()
                cnt+=2
            else:
                continue
    if cnt == len(a):
        print('YES')
    else:
        print('NO')

