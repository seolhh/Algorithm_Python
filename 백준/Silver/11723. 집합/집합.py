import sys
input = sys.stdin.readline
S = set()
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'add':
        S.add(int(order[1]))
    elif order[0] == 'remove':
        S.discard(int(order[1]))
    elif order[0] == 'check':
        print(1 if int(order[1]) in S else 0)
    elif order[0] == 'toggle':
        num = int(order[1])
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif order[0] == 'all':
        S = set(range(1, 21))
    elif order[0] == 'empty':
        S.clear()