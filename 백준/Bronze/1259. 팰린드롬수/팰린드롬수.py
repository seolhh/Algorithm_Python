while True:
    a = input()
    if a == '0':
        break

    length = len(a)

    if length % 2 == 1:
        if a[:length // 2] != a[:length // 2:-1]:
            print('no')
        else:
            print('yes')
    else:
        if a[:length // 2:] != a[:length // 2 - 1:-1]:
            print('no')
        else:
            print('yes')