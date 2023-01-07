def count_sheep(n):
    # your code
    sheep_count = []

    if n==0 | n<0:
        return ''
    else:     
        for i in range(1,n+1):
            sheep_count.append(str(i)+' sheep...')
        return ''.join(sheep_count)
