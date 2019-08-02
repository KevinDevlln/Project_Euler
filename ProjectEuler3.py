def Euler3(n=13195):
    for i in range(2,13195):
        while n % i == 0:
            n //= i
            print("%d is a factor, now we should test %d" % (i, n))
            if n == 1 or n == i:
                return i

Euler3()
