n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
idx = 0
# print(lst)
res = []
while len(lst)!=0:
    idx+=(m-1)
    idx = idx % len(lst) # 순환하기 위해서 나머지를 계속 입력, 만약 idx가 6이고 k-1이 5면 6%5 ==1 다시 인덱스1로 돌아
    res.append(lst.pop(idx))   # .pop(i)는 어떠한 리스트의 i번째 요요소(인덱스)를 삭제하는 것!!

print('<',', '.join(list(map(str,res))),'>',sep="")