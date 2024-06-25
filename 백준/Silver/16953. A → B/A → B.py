from collections import deque
import sys
input =sys.stdin.readline

a,b = map(int,input().split())

def bfs(a,b):
    q = deque()
    q.append((a,1))
    # print(q)

    while q:
        a,cnt = q.popleft()
        # print(a,cnt)

        if a>b:
            continue
        if a==b:
            print(cnt)
            break
        q.append((a*2,cnt+1))
        q.append((int(str(a)+'1'), cnt+1))
        # print(q)
    else:
        print(-1)

bfs(a,b)