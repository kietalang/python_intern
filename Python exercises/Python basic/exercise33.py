# sum of three given integers. However, if two values are equal sum will be zero

def sum_num(num1, num2, num3):
	result = 0
	if num1 == num2 or num2 == num3 or num1 == num3:
		return result
	else:
		result = num1 + num2 + num3

	return result

print(sum_num(1, 2, 3))