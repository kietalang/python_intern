# count the number of characters (character frequency)

def count_character(test_str):
	res = {i : test_str.count(i) for i in set(test_str)}
	return res

print(count_character("i am kiet"))