n = int(input())
stack =[]
op = []
Max = 0

for _ in range(n):
    num = int(input())
    if num > Max:
        for i in range((Max+1),(num+1)):
            stack.append(i)
            op.append('+')
        stack.pop() and op.append('-')
        Max = num
    else:
        if stack[-1] == num:
            stack.pop()
            op.append('-')
        else:
            print('NO')
            break
else:
    for K in op:
        print(K)