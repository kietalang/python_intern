# get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string

def get_string(s):
	if len(s) < 2:
		return ''
	return s[:2] + s[-2:]

print(get_string("kietalang")) #king
print(get_string("ki")) #kiki
print(get_string("k")) # empty