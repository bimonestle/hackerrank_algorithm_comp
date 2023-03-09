def kangaroo(x1, v1, x2, v2):
    print(x1, x2)
    if v1 <= v2 or x1 > x2:
        return 'NO'
    if x1 != x2:
        kangaroo(x1 + v1, v1, x2 + v2, v2)
        # print(x1, x2)
    return 'YES'