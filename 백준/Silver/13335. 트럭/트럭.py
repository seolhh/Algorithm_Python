import sys
input = sys.stdin.readline
n, w, L = map(int, input().split())
t = list(map(int, input().split()))
bridge = [0] * w
# print(bridge)
time = 0


while bridge: # 다리에 트럭이 없을때까지
    time += 1
    # print('시간추가',time)
    # 빈자리 만들기
    bridge.pop(0)
    if t:
        if sum(bridge) + t[0]<=L: #다리 위 트럭이랑 올라가려고 대기하는 트럭의 합이 최대하중 이하여야 함.
            bridge.append(t.pop(0))
            # print('트럭추가',bridge)
        else:
            bridge.append(0)
            # print('추가',bridge)

print(time)