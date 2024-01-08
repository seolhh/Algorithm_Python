# k층의 n호에 살려면 (k-1)층의 1~n 사람들 수의 합만큼 데려와 살아야한다.

t = int(input())

for _ in range(t):
    k = int(input()) #k층
    n = int(input()) #n호

    arr = [[0]*(n+1) for _ in range(k+1)]  #k층 n호의 배열 생성
    # print(arr)
    for j in range(n+1): #0층에 인원 배치
        arr[0][j]=j
    # print(arr)

    for floor in range(1,k+1): #한 층을 도는 것
        Sum = 0
        for room in range(1,n+1): #한 호수를 도는 것
            Sum+= arr[floor-1][room] #아래층의 호수값을 계속 더해서 Sum에 누적합
            arr[floor][room] =Sum  #그 Sum값이 내 층의 호수 값
    # for i in arr:
    #     print(*i)


    ans = arr[k][n]
    print(ans)