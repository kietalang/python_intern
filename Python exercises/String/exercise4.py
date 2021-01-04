# get a string from a given string where all occurrences of its first char have 
# been changed to '$', except the first char itself

def replace_char(string):
	first_char = string[0]
	replace_char = string.replace(first_char, "$")

	return string[:1] + replace_char

print(replace_char("rererrrr"))