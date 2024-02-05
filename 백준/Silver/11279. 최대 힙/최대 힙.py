import heapq
import sys
input = sys.stdin.readline

arr = []

n = int(input())
for i in range(n):
    x = int(input())
    if x ==0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr)) # 기본적으로 heapq는 최소힙이기 때문에 전체에 -를 하면 최대값을 구할 수 있다. 
    else:
        heapq.heappush(arr, -x) # 넣어줄때도 음수로 넣으면 된다 
