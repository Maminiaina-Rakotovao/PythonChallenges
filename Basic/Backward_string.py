# input --> output
# Ex: hello --> olleh
# Ex: Good --> dooG





# Create the backward function
def backward(text):
   
   # Create a void list to store the text
   backward_list = []
   
    for i in range(1,len(text)+1):
        backward_list.append(text[len(text)-i])
       
    return ''.join(backward_list)

