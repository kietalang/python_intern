def set_string(mine):
	if mine[:2] == "Is":
		return mine
	else:
		return "Is" + mine

my_string = "Is mine"

print(set_string(my_string))