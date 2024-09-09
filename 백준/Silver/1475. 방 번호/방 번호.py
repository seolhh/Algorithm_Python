dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

n = input()

for i in n:
    dic[int(i)]+=1

s = dic[6] + dic[9]
a = (s//2)+(s%2)


dic[6] = dic[9] =0
b = max(dic.values())
print(max(a,b))