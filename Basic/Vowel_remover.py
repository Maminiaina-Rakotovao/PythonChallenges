mylist=[]
vowel = ['a','i','o','u','e']
def shortcut(s):
    for i in s:
        mylist.append(i)
    for i in vowel:
        while i in mylist:
            mylist.remove(i)
    return ''.join(mylist)

