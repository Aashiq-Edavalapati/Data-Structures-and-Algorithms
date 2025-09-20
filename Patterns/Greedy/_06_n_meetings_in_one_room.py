def maxMeetings(start, end):
    n = len(start)
    meetings = [(start[i], end[i], i) for i in range(n)]
    meetings.sort(key=lambda meeting: meeting[1])

    scheduled = []
    lastEndTime = 0
    for meeting in meetings:
        if lastEndTime <= meeting[0]:
            scheduled.append(meeting[2])
            lastEndTime = meeting[1]
    
    return scheduled

if __name__ == '__main__':
    testCases = [
        ([0,3,1,5,5,8], [5,4,2,9,7,9])
    ]

    i = 0
    for start, end in testCases:
        print(f'TestCase {i}: {maxMeetings(start, end)}')
        i += 1