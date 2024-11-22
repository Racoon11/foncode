n = int(input())
fib = [0]*26
fib_otr = [0]*26
fib[1] = 1
if n >= 0:
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    print(fib[n])

else:
    fib_otr[1] = 1
    for i in range(2, -n+1):
        fib_otr[i] = fib_otr[i-2] - fib_otr[i-1]
    print(fib_otr[-n])
