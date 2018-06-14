#Project Euler 2
#Even Fibonacci numbers

i=2
fib = [1,2]

while sum(fib) <= 4000000000:
    fib.append(1)
    fib[i] = fib[i] + fib[i+1]
    i=i+1

print(fib)
