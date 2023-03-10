def kangaroo(x1, v1, x2, v2):
    while x1 != x2:
        if (x1 < x2 and v1 < v2) or (x1 > x2 and v1 > v2) or (v1 == v2):
            print('NO')
            return 'NO'
        x1 += v1
        x2 += v2
        print(x1, x2)
    print('YES')
    return 'YES'
    
kangaroo(2081, 8403, 9107, 8400)
# kangaroo(21, 6, 47, 3)