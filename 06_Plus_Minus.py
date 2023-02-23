def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for idx in range(len(arr)):
        if arr[idx] > 0:
            positive += 1
        elif arr[idx] < 0:
            negative += 1
            
    zero = len(arr) - negative - positive
    
    print(f'{(positive/len(arr)):.6f}')
    print(f'{(negative/len(arr)):.6f}')
    print(f'{(zero/len(arr)):.6f}')