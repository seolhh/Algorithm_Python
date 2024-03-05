n = int(input())
cnt = 0
for i in range(n):

    s=list(input())
    ans = [s[0]]
    # print(ans)
    for i in range(1,len(s)):
        if ans[-1]!=s[i]:
            if s[i] not in ans:
                ans.append(s[i])
                # print(s[i],'=s[i]')
            else:
                # print(s[i],'왜?')
                break

        else:
            ans.append(s[i])
    if ans==s:
        cnt+=1
print(cnt)
