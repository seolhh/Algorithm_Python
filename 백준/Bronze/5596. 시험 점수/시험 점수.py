mins = list(map(int,input().split()))
mans = list(map(int,input().split()))
if sum(mins) == sum(mans):
    print(sum(mins))
else:
    print(max(sum(mins),sum(mans)))