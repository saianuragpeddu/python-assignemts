def reverseLookup(dictionary, value):
    result_list = []
    for val in dictionary.keys():
        if dictionary[val] == value:
            result_list.extend(val)
    return sorted(result_list)

print(reverseLookup({'a':1, 'b':2, 'c':2}, 1))
