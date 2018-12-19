def getEvenNumbers(numbers): 
	test = []
	for i in numbers:
		odd = i % 2
		if odd == 0:
			test.append(i)
	return test



print(getEvenNumbers([1, 4, 8, 9]))
print(getEvenNumbers([]))
