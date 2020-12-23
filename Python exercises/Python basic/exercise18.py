# calculate the sum of three given numbers, if the values are equal then return three times of their sum

def calculate_num(a, b, c):
	
	sum = a + b + c

	if a == b ==c :
		sum = sum * 3

	return sum

print(calculate_num(3, 3, 3))