def calCumulativeSum(numbers):
    result_list = []
    i = 0
    while(i<=len(numbers)-1):
        result_list.append((sum(numbers[j] for j in range(0,i+1))))
        i+=1
    return result_list

print(calCumulativeSum([1,2,3]))
