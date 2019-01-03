def sortByLength(t, order):
    result = ()
    if(order == 'asc'):
        return sorted(t, key=len)
    elif(order == 'des'):
        for i in reversed(sorted(t, key=len)):
            result += (i,)
        return result
    else:
        return FALSE

print(sortByLength(('iOS', 'iPhone', 'iPad'), 'asc'))
print(sortByLength(('apple', 'orange', 'pear'), 'des'))
print(sortByLength(('begin', 'python', 'programming'), 'asc'))
