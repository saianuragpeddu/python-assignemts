def convertDictionary(d):
    if(d == {}):
        return []
    maxElem = max([int(s) for s in d.keys()])
    return [d.get(x, 0) for x in range(maxElem+1)]

print(convertDictionary({0: 1, 3: 2, 7: 3, 12: 4}))
