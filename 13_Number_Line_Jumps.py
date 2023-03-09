def kangaroo(x1, v1, x2, v2):
    # print(x1, v1, x2, v2)
    if v1 <= v2 and x1 <= x2:
        return 'NO'

    x1 += v1
    x2 += v2
    if x1 != x2:
        kangaroo(x1, v1, x2, v2)
        print(x1, x2)
    print(x1, x2)
    return 'YES'