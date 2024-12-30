m,n = map(int,input().split())
lst =[]
num_dict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}

ans1 = []
ans2 = []
for i in range(m,n+1):
    num = str(i)
    if len(num)==1:
        ans1.append((num,num_dict[num]))
    else:
        temp = num_dict[num[0]]+' '+num_dict[num[1]]
        ans2.append((num,temp))



sorted_pairs = sorted(ans1 + ans2, key=lambda x:x[1])
# print('sorted_pairs',sorted_pairs)


for i in range(0, len(sorted_pairs), 10):
    numbers = [pair[0] for pair in sorted_pairs[i:i + 10]]
    print(' '.join(numbers))