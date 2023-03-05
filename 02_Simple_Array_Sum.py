# Given an array of integers, find the sum of its elements.
# For example, if the array ar = [1,2,3].
# 1 + 2 + 3 = 6, so return 6.

def simpleArraySum(ar):
    sum = 0
    for numb in ar:
        sum += numb
    return sum

    # Shorter alternatives with built in function
    # return sum(ar)