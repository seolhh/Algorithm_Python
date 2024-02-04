import sys
input = sys.stdin.readline

import heapq

arr = []

n = int(input())

for i in range(n):
    x = int(input())
    if x ==0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr,x)
