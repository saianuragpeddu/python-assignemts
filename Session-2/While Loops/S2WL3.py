def countPages(num):
    total = 0
    i = 1
    while i<=num:
        page_no = str(i)
	total += page_no.count('1')
	i += 1
    return total

print(countPages(200))
