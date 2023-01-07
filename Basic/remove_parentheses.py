# Remove the parentheses

# In this kata you are given a string for example:

# "example(unwanted thing)example"

# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"

# "example(unwanted thing)example" --> "exampleexample"

# hello example (words(more words) here) something" --> "hello example  something"

# a(b(c)) -> a

def removeparentheses(s):
    counter_parentheses = 0
    result = ''
    for i in s:
        if i =='(':
            counter_parentheses += 1
        elif i ==')':
            counter_parentheses -= 1
        else:
            if counter_parentheses == 0:
                result += i
    return result
