def reverse(word):
    rev = ""
    for i in word:
        rev =i+rev
    return rev

print(reverse("apple"))
print(reverse("saianuragpeddu"))
