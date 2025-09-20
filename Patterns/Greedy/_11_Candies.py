def minCandies(ratings):
    n = len(ratings)
    candies = 1
    peak = 1
    i = 1
    while i < n:
        if ratings[i] == ratings[i - 1]:
            candies += 1
            i += 1
            continue

        peak = 1
        while i < n and ratings[i] > ratings[i - 1]:
            peak += 1
            candies += peak
            i += 1
        
        down = 1
        while i < n and ratings[i] < ratings[i - 1]:
            candies += down
            down += 1
            i += 1

        if down > peak:
            candies += down - peak
            
    return candies


if __name__ == '__main__':
    testCases = [
        [1,2,3],   # 6
        [1,3,2,1], # 7
        [0,2,4,3,2,1,1,3,5,6,4,0,0] # 
    ]

    i = 0
    for ratings in testCases:
        print(f'TestCase {i}: {minCandies(ratings)}')
        i += 1