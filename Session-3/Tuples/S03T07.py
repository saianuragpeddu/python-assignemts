def sortByIndex(a):
    c = sorted(a)
    b = ()
    for i in range(0,len(c)):
        b += (c[i][1],)
    return b

print(sortByIndex([(4,'Python'), (1, 'Welcome'), (3, 'Begin'), (2, 'To')]))
print(sortByIndex([(2,'Programming'), (3, 'is'), (1, 'Python'), (4, 'Fun')]))
