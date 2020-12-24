def historygram(values):
	for i in values:
		s = ""
		count = i
		while(count > 0):
			s += "*"
			count = count - 1
		print(s)

historygram([2, 6, 3, 1, 4])
