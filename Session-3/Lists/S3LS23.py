def getNumbers(num): 
    final_list = []
    for i in range(-num,num+1,2):
        final_list.append(i*i)
    return final_list

print(getNumbers(3))
