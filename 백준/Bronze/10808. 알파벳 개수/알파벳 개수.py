from string import ascii_lowercase

dic={}
for i in ascii_lowercase:
    dic[i]=0
n = input()
for i in n:
    dic[i]+=1

print(*list(dic.values()))
