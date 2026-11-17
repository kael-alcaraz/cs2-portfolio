# Code 3: Skip Multiples

for i in range(1, 16):
	if i % 3 == 0:
    # This utilises the modulo function, a Python builtin that determines the remainder of a number.
		continue
	else:
		print(i)
