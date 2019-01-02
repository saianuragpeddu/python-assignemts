def invertDictionary(d):
    newdict = {}
    for k, v in d.iteritems():
        newdict.setdefault(v, []).append(k)
    return newdict


print(invertDictionary({'a':2, 'b':1, 'c':2, 'd':1}))
