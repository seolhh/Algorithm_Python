
case=int(input())


for _ in range(case):
    y_win=0
    k_win=0
    for _ in range(9):
        y,k=map(int,input().split())
        y_win+=y
        k_win+=k
           
            
    if y_win>k_win:
        print('Yonsei')
    elif k_win>y_win:
        print('Korea')
    else:
        print('Draw')        