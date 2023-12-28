n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
# arr 2차원 배열을 정렬하는데, 키를 arr[0]번째를 기준으로 정렬
# sorted(arr,key=lambda arr:arr[0]) 으로도 작성 가능
arr.sort(key=lambda arr:int(arr[0]))

for i in range(n):
    print(arr[i][0],arr[i][1])
    