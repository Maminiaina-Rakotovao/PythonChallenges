def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return 1 if n==0 else fact
