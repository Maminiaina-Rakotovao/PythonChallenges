def longest(a1, a2):
    word = a1+a2
    s = sorted(word)
    print(s)
    for i in s:
        while s.count(i)>1:
            s.remove(i)
    return ''.join(s)

print(longest("aretheyhere", "yestheyarehere"))