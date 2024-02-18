num = int(input())

for i in range(num):
    a = input().split()
    ans =(float(a[0]))
    for j in range(len(a)):
        if a[j]=='@':
            ans *= 3
        elif a[j]=='%':
            ans += 5
        elif a[j]=='#':
            ans -= 7
    print("%0.2f"% ans)