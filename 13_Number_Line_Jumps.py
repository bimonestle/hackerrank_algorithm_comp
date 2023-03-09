def kangaroo(x1, v1, x2, v2):
    print(x1, x2)
    if x1 == x2:
        print('YES')
        return 'YES'
    if v1 <= v2 or x1 > x2:
        print('NO')
        return 'NO'
    kangaroo(x1+v1, v1, x2+v2, v2)

kangaroo(0, 3, 4, 2)
kangaroo(0, 2, 5, 3)