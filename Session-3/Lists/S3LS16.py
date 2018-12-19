def combine(la, lb):
    ans_list = []
    ans_list.extend(la)
    ans_list.extend(lb)
    ans_list.sort()
    return ans_list

print(combine(['a',1,'z'], [2,4,'y']))

