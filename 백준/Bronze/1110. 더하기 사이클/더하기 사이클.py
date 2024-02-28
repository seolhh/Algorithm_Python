N = int(input())
input_num=N
cnt= 0

while True:
    a = N // 10
    b = N % 10
    c = (a+b)%10
    N = b*10+c
    cnt+=1
    if input_num==N:
        break
print(cnt)