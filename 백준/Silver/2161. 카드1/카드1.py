from collections import deque
Q = deque()
n = int(input())
for i in range(n,0,-1):
    Q.append(i)
# print(Q)
S = []
while len(Q)>1:
    S.append(Q.pop())
    # print(Q,"Q")
    Q.appendleft(Q.pop())
print(*(S+list(Q)))







