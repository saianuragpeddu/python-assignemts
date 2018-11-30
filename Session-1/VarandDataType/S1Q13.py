# Write a function that does a decimal to hexadecimal conversion.
# Hint: Make use of "%x" for hexadecimal format.
def dec2hex(num): 
	gap = "0x0" + "%x" % num
	if len(gap) > 4:
	  sol = "0x" + "%x" % num
	  return sol
	else:
	  return gap
	  
print(dec2hex(34))
print(dec2hex(0))
print(dec2hex(10))
