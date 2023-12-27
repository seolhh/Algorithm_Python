num1 = int(input())
num2 = int(input())
num3 = int(input())
ans = num1 * num2 * num3

lst =[]

for i in range(10):
    lst.append(0)

for i in str(ans):
    lst[int(i)]+=1


for i in lst:
    print(i)

    