def insertInterval(intervals, newInterval):
    newIntervals = []
    # Left part (Non-overlapping)
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:
        newIntervals.append(intervals[i])
        i += 1
    
    # Middle part (Overlapping)
    start, end = newInterval[0], newInterval[1]
    while i < n and intervals[i][1] < newInterval[1]:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    newIntervals.append([start, end])

    # Right part (Non-overlapping)
    while i < n:
        newIntervals.append(intervals[i])
        i += 1

    return newIntervals

if __name__ == '__main__':
    testCases = [
        ([[1,3], [6,9]], [2,5]), # Expected o/p: [[1,5]. [6,9]]
        ([[1,2],[3,4],[6,7],[8,10],[12,16]], [5,8]), # Expected o/p: [[1,2], [3,4], [5,10], [12, 16]]
        ([[1,2],[3,4],[5,7],[8,10],[12,16]], [6,8]), # Expected o/p: [[1,2], [3,4], [5,10], [12, 16]]
        ([[1,2],[3,4],[7,7],[8,10],[12,16]], [5,6])  # Expected o/p: [[1,2], [3,4], [5, 6], [7,7], [8,10], [12,16]]
    ]

    i = 0
    for intervals, newInterval in testCases:
        print(f'TestCase {i}: {insertInterval(intervals, newInterval)}')
        i += 1