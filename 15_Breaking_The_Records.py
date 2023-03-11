# Maria plays college basketball and wants to go pro.
# Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record
# for most points and least points in a game.
# Points scored in the first game establish her record for the season,
# and she begins counting from there.

# Example
# scores = [12, 24, 10, 24]
# Scores are in the same order as the games played. She tabulates her results as follows:
#                                               Count
# Game      Score       Minimum     Maximum     Min     Max
#   0       12          12          12          0       0
#   1       24          12          24          0       1
#   2       10          10          24          1       1
#   1       24          10          24          1       1
# 
# result = [1, 1]



def breakingRecords(scores):
    # Variables initialization
    minn = 0
    countMin = 0
    maxx = 0
    countMax = 0
    result = []
    
    for idx in range(len(scores)):
        # No comparation. Just value initialization
        if idx == 0:
           minn = scores[idx]
           maxx = scores[idx]
        
        # replace minn value if it's lower than
        # its previous value and add its counter
        if scores[idx] < minn:
            countMin += 1
            minn = scores[idx]
        
        # replace maxx value if it's higher than
        # its previous value and add its counter
        elif scores[idx] > maxx:
            countMax += 1
            maxx = scores[idx]

    # assign final values to an empty array and return it
    result.extend([countMax, countMin])
    return result