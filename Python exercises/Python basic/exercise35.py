# return true if the two given integer values are equal or their sum or difference is 5

def check_num(num1, num2):
	sum = num1 + num2
	diff = num1 - num2
	if num1 != num2 or sum != 5 or diff != 5:
		return "False"
	else:
		return "True"

print(check_num(2, 3))