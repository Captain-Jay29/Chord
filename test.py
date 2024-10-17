

def keypad(s):

	dial = [[]]*9
	ptr = 0

	unique = set(s)

	for i in unique:

		if ptr > 8:
			break

		dial[ptr] += i

		print(dial)

		print(f'i: {i}')
		print(f'ptr: {ptr}')
		

		ptr += 1


	# print(dial)



keypad('abacadefghibj')