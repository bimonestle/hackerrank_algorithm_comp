def kangaroo(x1, v1, x2, v2):
    print(x1, x2)
    if x1 == x2:
        print('YES')
        return 'YES'
    elif (x1 < x2 and v1 < v2) or (x1 > x2 and v1 > v2) or (v1 == v2):
        print('NO')
        return 'NO'
    else:
        return kangaroo(x1+v1, v1, x2+v2, v2)