# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# [[1 2 3],
# [4 5 6],
# [9 8 9]]

# The left-to-right diagonal = 1 + 5 + 9 = 15.
# The right to left diagonal = 3 + 5 + 9 = 17.
# Their absolute difference is |15 - 17| = 2.

# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for idx in range(len(arr)):
        # sum diagonal left to right array
        # pattern: [0][0], [1][1], [2][2]
        sum1 += arr[idx][idx]

        # sum diagonal right to left array
        # pattern: [0][2], [1][1], [2][0]
        sum2 += arr[idx][len(arr)-1-idx]
        
    return abs(sum1-sum2)