import sys

n = int(input())
lst = set()

for i in range(n):
    lst.add(sys.stdin.readline().rstrip())

lst_sorted = sorted(lst, key=lambda x: (len(x), x))

for i in lst_sorted:
    print(i)
