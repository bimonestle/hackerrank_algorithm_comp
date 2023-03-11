def breakingRecords(scores):
    minn = 0
    countMin = 0
    maxx = 0
    countMax = 0
    result = []
    
    for idx in range(len(scores)):
        if idx == 0:
           minn = scores[idx]
           maxx = scores[idx]
           
        if scores[idx] < minn:
            countMin += 1
            minn = scores[idx]
        elif scores[idx] > maxx:
            countMax += 1
            maxx = scores[idx]

    result.append(countMax)
    result.append(countMin)
    return result