# Addition
def add(x, y):
	return x + y

# Multiplication
def mult(x, y):
	return x * y

# Subtraction
def sub(x, y):
	return x - y

# Division
def div(x, y):
	if y == 0:
		raise ValueError('Can\'t divide by zero')
	return x / y