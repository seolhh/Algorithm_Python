word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
n = input()
cnt=0


for i in word:
    if i in n:
        n=n.replace(i,'?')
print(len(n))