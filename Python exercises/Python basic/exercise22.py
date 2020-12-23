def count_number_inlist(numlist):
	count = 0 

	for i in numlist:
		if i == 4:
			count += 1
	return count

my_num_list = [1, 4, 5, 6, 4] #expected result is 2

print(count_number_inlist(my_num_list))