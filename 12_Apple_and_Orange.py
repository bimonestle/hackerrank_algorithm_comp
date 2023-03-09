def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    
    for apple in apples:
        appleDrop = a + apple
        if appleDrop >= s and appleDrop <= t:
            appleCount += 1
    for orange in oranges:
        orangeDrop = b + orange
        if orangeDrop >= s and orangeDrop <= t:
            orangeCount += 1
    
    print(appleCount)
    print(orangeCount)