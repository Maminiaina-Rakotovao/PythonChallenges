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
    print(s)


n1 = input('Enter the first number: ')
n1 = int(n1)
n2 = input('Enter the first number: ')
n2 = int(n2)
get_sum(n1,n2)
