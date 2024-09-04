import sys
input = sys.stdin.readline

n = int(input())
stack = [0]

for j in range(n):
    i = int(input())
    if i != 0:
        stack.append(i)
        # print('넣는다',i)
    else:
        a=stack.pop()
        # print('뺀다',a)

print(sum(stack))
