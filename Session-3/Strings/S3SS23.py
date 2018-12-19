def splitWord(word, numOfChar):
 	output = []
 	for i in range(0,len(word),numOfChar):
 		output.append(word[i:i+numOfChar])
 	return output

print(splitWord('apple', 2))
print(splitWord('apple', 1))
