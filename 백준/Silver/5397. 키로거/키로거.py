n = int(input())

for _ in range(n):
    stack = []
    box = []
    t = input()
    # print(t)
    for i in t:
        if i == '<':
            if stack:
                a=stack.pop()
                box.append(a)
        elif i =='>':
            if box:
                stack.append(box.pop())
        elif i =='-':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    print(''.join(stack+ box[::-1]))  #커서가 마지막에서 끝나지 않는경우는, box에 남아있는 값이 있을 수도 있다.
     # 엣지케이스 : ' abc<<d>e> '

