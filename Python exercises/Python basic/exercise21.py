def check_num(num):
	if num % 2 == 0:
		print("Your given number is even")
	else: 
		print("Your given number is odd")

my_num = int(input("Give me a number: "))

check_num(my_num)