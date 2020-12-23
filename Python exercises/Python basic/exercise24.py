# check vowel test given

def check_vowel(test):
	vowel = "ueoai"
	if test in vowel:
		return test + " is vowel"
	else:
		return test + " is not vowel"

print(check_vowel("a"))