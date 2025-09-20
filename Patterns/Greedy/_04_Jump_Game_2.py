def minJumps(arr):
    jumps, l, r = 0, 0, 0
    n = len(arr)
    while r < n -1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(i + arr[i], farthest)
        l = r + 1
        r = farthest
        jumps += 1

    return jumps

if __name__ == '__main__':
    testCases = [
        [2,3,1,4,1,1,1,2]
    ]

    i = 0
    for arr in testCases:
        print(f'TestCase {i}: {minJumps(arr)}')
        i += 1