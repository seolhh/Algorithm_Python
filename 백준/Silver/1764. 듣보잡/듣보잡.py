import sys
input = sys.stdin.readline
n,m = map(int,input().split())
no_hear ={input().rstrip():1 for _ in range(n)}

for _ in range(m):
     i = input().rstrip()
     if no_hear.get(i) ==None:
         continue
     else:
         no_hear[i]+=1

answer = []
for key,val in list(no_hear.items()):
    if val ==2:
        answer.append(key)

print(len(answer))
for i in sorted(answer):
    print(i)
