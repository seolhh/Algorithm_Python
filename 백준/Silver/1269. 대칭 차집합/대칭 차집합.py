import sys
input = sys.stdin.readline

a,b = map(int,input().split())
a_lst = set(map(int,input().split()))
b_lst = set(map(int,input().split()))
a_b=a_lst-b_lst
b_a=b_lst-a_lst
print(len(a_b)+len(b_a))