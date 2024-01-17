n = int(input())
# 무조건 sort를 해서 앞에 최대한 적은 수가 와야 누적할 때 값이 적어진다 !!
lst =sorted(list(map(int,input().split())))
# print(lst)
add = all =  0



# 누적합
for i in lst:
    add = add+i
    all+=add

print(all)
