# There will be two arrays of integers.
# Determine all integers that satisfy the following two conditions:

# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array

# These numbers are referred to as being between the two arrays.
# Determine how many such numbers exist.

# Example:
# a = [2, 6]
# b = [24, 36]

# There are two numbers between the arrays: 6 and 12.
# 6 % 2 == 0, 6 % 6 == 0, 24 % 6 == 0, 36 % 6 == 0.
# 12 % 2 == 0, 12 % 6 == 0, 12 % 6 == 0, 12 % 6 == 0.
# return 2.

def getTotalX(a, b):
    
    considered = []
    result = []
    a_lastEl = a[len(a)-1]
    b_firstEl = b[0]
    
    # sort the elements to ease determining
    # the inbetween numbers of a and b
    a.sort()
    b.sort()
    
    # get the considered numbers
    for numb in range(a_lastEl, b_firstEl+1):
        if numb <= b_firstEl:

            # check if the considered numbers are factor of b
            if all(el % numb == 0 for el in b):
                considered.append(numb)

    # evaluate the considered numbers
    for number in considered:
        # check if the elements in a are factor of considered numbers
        if all(number % elA == 0 for elA in a):
            result.append(number)
            
    return len(result)