def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for idx in range(len(arr)):
        sum1 += arr[idx][idx]
        sum2 += arr[idx][len(arr)-1-idx]
        
    return abs(sum1-sum2)