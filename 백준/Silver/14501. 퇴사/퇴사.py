# 가장 마지막 날 +1은 상담 불가
# 뒤에부터 보면서 가장 마지막날(N)을 넘어가는 경우 x

N=int(input())
T=[]
P=[]
dp = [0] * (N + 1)
max_money = 0
for n in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

# print(T,P)

for i in range(N-1, -1,-1):
    # print(i)
    time=T[i]+i  ##왜? T는 가능한 시간들을 모아놓은 리스트니까 계산 값이 N을 넘어가면 안됨
    # print(time)
    if time <=N :
        dp[i]=max(P[i]+dp[time], max_money)  #여기서 max_money를 왜 넣어주는지
        # print(dp[i])
        max_money = dp[i]
    else:
        dp[i]=max_money
print(max_money)
