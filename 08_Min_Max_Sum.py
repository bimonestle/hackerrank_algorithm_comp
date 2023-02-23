# Given five positive integers, find the minimum and maximum values
# that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values
# as a single line of two space-separated long integers.

# Example:
# arr = [1, 3, 5, 7, 9]
# Minimum Sum = [1, 3, 5, 7] = 16
# Maximum Sum = [3, 5, 7, 9] = 24

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))