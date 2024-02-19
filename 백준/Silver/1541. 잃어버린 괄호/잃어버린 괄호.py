import re

lst = input()

new_lst = lst.split('-') # 가장 큰 '-'를 기준으로 다 나눔
# print(new_lst)

first = sum(map(int,new_lst[0].split('+'))) # 최초로 나오는 '-' 앞의 수에서 뒤에 나오는 모든 수들을 빼야하니까 따로처리  

for i in new_lst[1:]:
    first-=sum(map(int,i.split('+'))) # '+' 기준으로 다 나눠서 그 수를 다 더함, 가장 앞의 수에서 뒤에 나오는 애들 다 빼줌 

print(first)
