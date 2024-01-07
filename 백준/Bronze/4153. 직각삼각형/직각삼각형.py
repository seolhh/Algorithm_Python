while True:
    a,b,c = sorted(list(map(int,input().split())))
# 가장 긴 변이 빗변이기 때문에 정렬
    if a== b== c == 0:
        break
    elif (a**2) + (b**2) == c**2:
        print('right')
    else:
        print('wrong')