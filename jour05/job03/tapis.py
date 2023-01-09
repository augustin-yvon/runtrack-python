def tapis(n):
    a = '+'
    for i in range(n+1):
        a += '-'
    a += '+'

    print(a)

    for i in range(n+1):
        b = ''
        for j in range(n-i):
            b += '#'
        b += ' '
        for j in range(i):
            b += '#'
        print("|" + b + '|')

    print(a)

tapis(10)