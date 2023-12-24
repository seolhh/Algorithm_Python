# input값을 문자열로 받아서 길이를 나누기 2
# 슬라이싱 사용해서 해당 값 ㄷ ㅏ 더하고 그 다음 슬라이싱 사용해서 해당 값 다 더함
# error : 슬라이싱은 문자열이나 리스트에서만 사용 가능 하다.
# ->input값을 리스트에 넣어서 슬라이싱 사용
# 두개의 합이 같으면 lucky 출력


N = input()# 문자열
N_lst = list(map(int,list(N))) # 문자열 -> int로 바꿔서 다시 리스트에 넣기
n_len =len(N_lst)//2 # 길이 반으로 나눈 몫

ans1=sum(N_lst[:n_len])
ans2=sum(N_lst[n_len :])

if ans1==ans2:
    print("LUCKY")
else:
    print("READY")