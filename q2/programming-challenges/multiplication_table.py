# Code 4:	Multiplication Table Generator

def show_table(number):
  # This creates the function show_table.
	for i in range (1, 11):
		product = number * i
		print(f"{number} multiplied by {i} equals {product}.")
    # This is to print the multiplication table step.
number = int(input("Give me a number: "))
show_table(number)
