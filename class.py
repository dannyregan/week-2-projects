from random import random
from random import randrange

def countPositiveIntegers(arr):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

def uniqueElements(A):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return False
    return True

def binaryDigitCount(n):
    count = 1
    while n > 1:
        count += 1
        n = n // 2
    return count

# For binaryDigitCount function
for n in [3,23,32,345,1023,1024, 1073741824]:
    print(f"The number of bits for {n} is: {binaryDigitCount(n)} ({bin(n)[2:]})")

# For countPositiveIntegers function
# A = []
# for i in range(100):
#     A.append((random() - 0.5) * 100)

# For uniqueElements function
# A = []
# for i in range(10000):
#     A.append(randrange(1000000000))
# if uniqueElements(A):
#     print("All elements are unique.")
# else:
#     print("Elements are not unique.")

# print(f"There are {countPositiveIntegers(A)} positive numbers.")