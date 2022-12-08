# input --> output
# Ex: hello --> olleh
# Ex: Good --> dooG


# Create a void list to store the text
backward_list = []

# Create the backward function
def backward(text):
   # j = 1
    for i in range(1,len(text)+1):
        backward_list.append(text[len(text)-i])
       # j = j + 1
    print(''.join(backward_list))

n = input('Enter: ')

backward(n)
