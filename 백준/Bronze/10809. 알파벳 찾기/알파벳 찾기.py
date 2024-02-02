s = input()
alpha_dic = {chr(i): -1 for i in range(97, 123)}  # 알파벳 소문자에 해당하는 ASCII 코드 범위 설정

for idx, char in enumerate(s):
    if alpha_dic[char] == -1:  # 해당 알파벳이 이전에 등장하지 않았다면
        alpha_dic[char] = idx  # 최초 등장 위치로 업데이트

print(*alpha_dic.values())