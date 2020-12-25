# sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def sum(num1, num2):

	result = num1 + num2

	if result in range(15, 20):
		return 20
	else:
		return result

print(sum(9, 8))
print(sum(5, 8))