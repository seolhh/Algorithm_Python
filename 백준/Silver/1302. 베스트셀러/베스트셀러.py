n = int(input())
dic = {}
for _ in range(n):
    title=input()
    if title not in dic:
        dic[title]=1
    else:
        dic[title] += 1

a=sorted(dic.items(),key=lambda x:(-x[1],x[0]))  #딕셔너리 정렬 다중조건, lambda x:x의 어떤거 기준, 만약 기준이 2개이상이면 ()안에 넣
print(a[0][0])