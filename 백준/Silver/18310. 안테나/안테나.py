N = int(input())
h_lst = sorted(list(map(int, input().split())))

ans = 0
mid=len(h_lst)//2
if N%2==0:
    num=h_lst[mid-1]
else:
    num = h_lst[mid]


print(num)