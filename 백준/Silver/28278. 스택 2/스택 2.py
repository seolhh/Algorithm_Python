import sys

input= sys.stdin.readline

n = int(input().rstrip())
stack = []

for _ in range(n):
    m = input().split()
    if int(m[0])==1:
        stack.append(int(m[1]))
    elif int(m[0])==2:
        if stack:
            print(stack.pop())

        else:
            print(-1)
    elif int(m[0])==3:
        print(len(stack))
    elif int(m[0])==4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif int(m[0])==5:
        if stack:
            print(stack[-1])
        else:
            print(-1)