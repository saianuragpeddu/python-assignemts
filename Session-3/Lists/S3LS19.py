def combineList(list1, list2):
    ans_list = []
    ans_list.extend(list1)
    ans_list.extend(list2)
    return ans_list

print(combineList([1,2], [3,4]))
