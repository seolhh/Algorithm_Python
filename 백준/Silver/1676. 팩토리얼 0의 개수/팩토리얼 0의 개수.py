n = int(input())
ans = 1
for i in range(1,n+1):
    ans*=i
    # print(ans)

str_ans=str(ans)

cnt =0
for i in str_ans[::-1]:
    if i =='0':
        cnt+=1
    else:
        break
print(cnt)