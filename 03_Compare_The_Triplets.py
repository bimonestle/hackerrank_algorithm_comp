def compareTriplets(a, b):
    alice = 0
    bob = 0
    result = []

    for idx in range(len(a)):
        if a[idx] > b[idx]:
            alice += 1
        elif a[idx] < b[idx]:
            bob += 1
    result.extend([alice, bob])

    return result

