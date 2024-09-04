import sys
input = sys.stdin.readline

n = int(input())
stack = []

for j in range(n):
    i = list(input().split()) #리스트안에 담아야, split기준으로 뒤에 숫자가 있던 없던 출력 가능.

    if i[0] =='push':
        stack.append(i[1])
    elif i[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.pop()
            print(p)
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] =='empty':
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif i[0] =='top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)