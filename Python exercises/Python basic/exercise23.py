# get the n (non-negative integer) copies of the first 2 characters of a given string 
# and return the n copies of the whole string if the length is less than 2

def copy_charater(mystring, n):
	if len(mystring) <= 2:
		return mystring * n
	else:
		return mystring[:2] * n

mystring = "kiet"

print(copy_charater(mystring, 2))