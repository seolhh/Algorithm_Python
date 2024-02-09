from collections import deque
import sys

input = sys.stdin.readline

Q = deque()
n = int(input())

for i in range(n):
    order = input().split()
    if order[0] == "push_front":
        Q.appendleft(order[1])
    elif order[0] =="push_back":
        Q.append(order[1])
    elif order[0] =="pop_front":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif order[0] =="pop_back":
        if len(Q) ==0:
            print(-1)
        else:
            print(Q.pop())
    elif order[0] =="size":
        print(len(Q))
    elif order[0] == "empty":
        if len(Q) ==0 :
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif order[0] == "back":
        if len(Q) == 0 :
            print(-1)
        else:
            print(Q[-1])

