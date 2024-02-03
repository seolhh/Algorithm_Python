from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    L = list(map(int, input().split()))
    Q = deque((i, p) for i, p in enumerate(L))  # 문서의 순서와 중요도를 데크에 추가

    cnt = 0
    while True:
        front = Q.popleft()
        if any(front[1] < doc[1] for doc in Q):  # 현재 문서의 중요도보다 높은 중요도를 가진 문서가 있는지 확인
            Q.append(front)
        else:
            cnt += 1
            if front[0] == m:  # 찾고자 하는 문서가 출력되면 출력 순서를 출력하고 반복문 종료
                print(cnt)
                break
