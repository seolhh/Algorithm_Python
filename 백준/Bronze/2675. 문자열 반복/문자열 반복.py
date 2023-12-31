
n=int(input())
for _ in range(n):
    a,b=map(str,input().split())
    a=int(a)
    st=''
    for i in b:
        st+=i*a
    print(st)