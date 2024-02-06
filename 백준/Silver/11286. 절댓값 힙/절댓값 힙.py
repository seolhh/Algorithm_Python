import sys
import heapq
input = sys.stdin.readline

arr = []
n = int(input())
for i in range(n):
    x = int(input())
    if x != 0 :
        heapq.heappush(arr,(abs(x),x))  #입력받은 수의 절댓값,원래값을 함께 튜플형태로 넣음.
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])  # arr에 튜플형태로 있는 것 중, 원래값을 보여줘야 하니까 arr[1]

