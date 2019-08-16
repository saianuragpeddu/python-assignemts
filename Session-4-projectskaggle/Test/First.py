# First question

fname = ("C:\\Users\\anura\\GitHub\\python-assignments\\Session-4-projectskaggle\\Test\\Input\\count.txt")

num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)


# Second Question

name1 = ("C:\\Users\\anura\\GitHub\\python-assignments\\Session-4-projectskaggle\\Test\\Input\\name1.txt")
name2 = ("C:\\Users\\anura\\GitHub\\python-assignments\\Session-4-projectskaggle\\Test\\Input\\name2.txt")
name3 = ("C:\\Users\\anura\\GitHub\\python-assignments\\Session-4-projectskaggle\\Test\\Input\\name3.txt")

fin = open(name1, "r")
data1 = fin.read()
fin.close()

fon = open(name2, "r")
data2 = fon.read()
fon.close()

fout = open(name3, "a")
fout.write(data1)
fout.write(data2)
fout.close()

# Third Question

Number = int(input("Please Enter any Number: "))

Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)

Number = int(input("Please Enter any Number: "))

Sum = 0
while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)

# print Contiguous character and occurrence in python

charseq = 'Hello World avccc'
distros = { c:1 for c in charseq  }

for c in range(len(charseq)-1):
    if charseq[c] == charseq[c+1]:
        distros[charseq[c]] += 1

print(distros)

# print all permutations of a string withput library function

def permute(data, i, length):
    if i==length:
        print(''.join(data) )
    else:
        for j in range(i,length):
            #swap
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]


string = "ABC"
n = len(string)
data = list(string)
permute(data, 0, n)

# sort array of data without library

mylist = [5, 3, 7, 2, 8, 4]
print(mylist)
n = len(mylist)
for i in range(n):
    for j in range(1, n-i):
        if mylist[j-1] < mylist[j]:
            (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist)

# Explain python multiple inheritance using any example



# write a program for fibonacci number using python quperators

def fibonacci(n):
    FibArray = [0, 1]
    while len(FibArray) < n + 1:
        FibArray.append(0)
    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)
        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]

print(fibonacci(9))
