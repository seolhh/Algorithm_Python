from collections import deque

n = int(input())
q = deque()
for i in range(1,n+1):
    q.append(i)

while len(q) > 1:  #1이되기 전까지 돌아야 함. 
    q.popleft()
    q.append(q.popleft())

print(q[0])