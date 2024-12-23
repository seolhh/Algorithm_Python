n = int(input())
lst = list(map(int,input().split()))


left = 0
right = n-1
min_sum = abs(lst[left]+lst[right])
result = [lst[left],lst[right]]

while left < right:
    current = lst[left] + lst[right]
    if current == 0:
        result = [lst[left], lst[right]]
        break

    if abs(current) < min_sum:
        min_sum = abs(current)
        result = [lst[left], lst[right]]

    if current < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])