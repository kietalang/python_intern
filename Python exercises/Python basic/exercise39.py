# compute the future value of a specified principal amount, rate of interest, and a number of years

def future_value(a, i, y):
	return a*((1+(0.01*i)) ** y)

# test data
print(round(future_value(1000, 3.5, 7), 2))