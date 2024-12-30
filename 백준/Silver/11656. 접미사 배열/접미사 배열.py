s = input()
lst=[]

for i in range(len(s)):
    lst.append(s[i:])
    lst.sort()

for j in lst:
    print(j)