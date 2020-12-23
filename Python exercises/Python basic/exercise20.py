# give a string and n (non-negative integer) then copy the string by n times

def copy_string(my_string, n):

	result = ""
	for i in range(n):
		result += my_string
	return result

my_string = "I am kiet"
n = 3

print(copy_string(my_string, n))