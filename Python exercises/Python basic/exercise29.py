def get_list_different(list1, list2):
	list_different = []
	for item in list1:
		if item not in list2:
			# Append is use to add an elemement to the list
			list_different.append(item)
	print(list_different)

list1 = ["Red", "Blue", "Black"]
list2 = ["White", "Red", "Blue"]

get_list_different(list1, list2)