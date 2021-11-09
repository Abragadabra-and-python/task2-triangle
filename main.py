rows = int(input('Enter number of rows >>> '))
spaces = (rows * 2) - 2 # Counting the number of spaces

if rows == 0 or rows < 0:
	print(ValueError('Are you a fool, how can I draw such a triangle?'))
else:
	for i in range(0, rows):
		for j in range(0, spaces):
			print(end=' ') # Displaying spaces
		spaces -= 1
		for j in range(0, i + 1):
			print('* ', end='') # Displaying stars
		print('')