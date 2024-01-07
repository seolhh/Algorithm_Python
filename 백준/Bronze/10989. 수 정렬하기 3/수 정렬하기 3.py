import sys

n = int(sys.stdin.readline())
count = [0] *10001
    # 모든 숫자를 나열하면 메모리가 크니까 직접적으로 나오는 숫자 10000개에 대해서 먼저 만들어놓는다.

for i in range(n):
    num = int(sys.stdin.readline())
    count[num]+=1
        # 만개의 숫자 중에 입력들어온 값은 해당 숫자에 cnt+=1올려준다.

for i in range(1,10001):
# 만개를 다 돌면서
    for _ in range(count[i]):
# 만약 count[7]자리에 0이있다면 for문이 안돌고 넘어감.
        print(i)