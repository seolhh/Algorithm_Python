import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = {}
for _ in range(n):
    word = input().rstrip()

    if len(word)>=m:
        # print(word)
        if word not in s:
            s[word]=1
        else:
            s[word]+=1

# print('ss',s)


# 딕셔너리 여러 조건으로 sorted
ans = list(sorted(s.items(),key=lambda x:(-x[1],-len(x[0]),x[0])))

# 튜플 출력하기
# ans는 튜플이기 때문에,
for key,val in ans:
    print(key)