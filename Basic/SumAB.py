def get_sum(a,b):
    s = 0
    if a < b:
        while a <= b:
            s = s + a
            a += 1
    else:
        while b <= a:
            s = s + b
            b += 1
    return s


n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the first number: '))
get_sum(n1,n2)
