import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = list(map(int,input().split()))


cumusum = [0] * (n + 1)
for i in range(1, n + 1):
    cumusum[i] = cumusum[i - 1] + lst[i - 1]
    # print(cumusum[i - 1], lst[i - 1])
    # print(cumusum,'Sum')

for _ in range(m):
    i,j = map(int,input().split())
    result = cumusum[j]-cumusum[i-1]
    print(result)


    #누적합 푸는 방식이라는데 잘 모르겠음...
