def hasSameContent(t1, t2):
     i = 1
     if(len(t1) != len(t2)):
         return False
     else:
         return sorted(t1)==sorted(t2)

print(hasSameContent((1,2), (1,2)))
print(hasSameContent((1,3), (1,2)))
