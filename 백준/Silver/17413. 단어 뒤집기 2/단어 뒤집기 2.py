s = input()

temp = []
answer = []

for i in range(len(s)):
    # 닫힌 괄호가 나오면
    if s[i] == '>':
        temp.append('>')
        
        answer.append(''.join(temp))
     
        temp = []
    # 열린 괄호가 나왔는데 이전에 입력된 것들이 있다면
    elif s[i] == '<' and temp:
      
        temp.reverse()
        answer.append(''.join(temp))
        
        temp = [s[i]]
    # 공백 문자인데 괄호 밖이라면
    elif s[i] == ' ' and '<' not in temp:
     
        temp.reverse()
        answer.append(''.join(temp))
        answer.append(' ')
       
        temp = []
    else:
        temp.append(s[i])

if temp: 
    temp.reverse()
    answer.append(''.join(temp))

print(''.join(answer))