def noOfNonOverlappingIntervals(intervals):
    intervals.sort(key=lambda interval: interval[1])

    count = 0
    lastEndTime = 0
    for interval in intervals:
        if lastEndTime > interval[0]:
            count += 1
        else:
            lastEndTime = interval[1]
    
    return count

if __name__ == '__main__':
    testCases = [
        [(0,5), (3,4), (1,2), (5,9), (5,7), (7,9)],
        [(1,2),(2,3),(3,4)]
    ]

    i = 0
    for intervals in testCases:
        print(f'TestCase {i}: {noOfNonOverlappingIntervals(intervals)}')
        i += 1