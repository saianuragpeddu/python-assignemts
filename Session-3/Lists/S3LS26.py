def getAboveAverage(nums):
    return [ x for x in nums if x > (sum(nums)/float(len(nums))) ]

print(getAboveAverage([1,2,3,4]))
