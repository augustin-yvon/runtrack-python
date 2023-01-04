def nombre_premier(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in range(1001):
    if nombre_premier(i):
        print(i)

