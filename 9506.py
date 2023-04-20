while True:
    a = int(input())
    if a == -1:
        break
    b = []
    for i in range(1, a):
        if a % i == 0:
            b.append(i)
    if sum(b) == a:
        print(a, ' = ', ' + '.join(str(i) for i in b), sep='')
    else:
        print(a, 'is NOT perfect.')
