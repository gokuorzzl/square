n = input('사각형의 한면은 얼마?')
n = int(n)
if 1<=n<3:
    for n in range(n, 0, -1):
        print('*'*a)
if n >=3:
    print('*'*n)
    for a in range(0, n-2):
        print('*',' '*(n-2),'*', sep='')
    print('*'*n)
