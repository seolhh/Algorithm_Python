import sys
from collections import deque

input = sys.stdin.readline
n , m = map(int,input().split())
lst = deque(map(int,input().split())) #내가 뽑고 싶은 수
Q=deque(range(1,n+1))

cnt = 0
while lst:
    if lst[0]==Q[0]:
        Q.popleft()
        lst.popleft()
    else:
        # print(lst[0],'나는큐',Q[0],'뭐야')
        if Q.index(lst[0])>(len(Q)/2):
            Q.appendleft(Q.pop())
            cnt+=1
        else:
            Q.append(Q.popleft())
            # print(Q,'QQQ')
            cnt+=1
print(cnt)