n = int(input())
a_lst = sorted(list(map(int,input().split())),reverse=True)
b_lst = sorted(list(map(int,input().split())))
# print(a_lst,b_lst)

Sum = 0
for i in range(n):
    Sum+=a_lst[i]*b_lst[i]

print(Sum)