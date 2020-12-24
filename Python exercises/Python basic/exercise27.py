def concat_element(values):
	seperator = ' ' # Create a space between a letter
	return seperator.join([str(element) for element in values])

elements = ["My", 1, "is", "Kiet"] #expected result My 1 is Kiet

print(concat_element(elements))