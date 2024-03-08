t = int(input())
al={'A','B',"C","D",'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

for _ in range(t):
    s=set(input())
    ans=al-s

    sum = 0

    for i in ans:
        sum+=ord(i)
    print(sum)