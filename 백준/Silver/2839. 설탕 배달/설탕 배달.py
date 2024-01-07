n = int(input())
cnt_5 = 0
cnt_3 = 0

if n%5==0:
    cnt_5 = n // 5
    print(cnt_5)
else:
    while True:
        if n < 0:
            print(-1)
            break
        if (n - 3) % 5 == 0:
            cnt_5 = (n-3) // 5
            cnt_3 += 1
            print(cnt_5 + cnt_3)
            break

        cnt_3 += 1
        n = n - 3
