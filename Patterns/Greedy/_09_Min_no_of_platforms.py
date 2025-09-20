def minPlatforms(arr, dep):
    arr.sort()
    dep.sort()
    n = len(arr)

    i, j = 0, 0
    platforms = 0
    currPlatforms = 0
    while i < n:
        if arr[i] < dep[j]:
            currPlatforms += 1
            platforms = max(platforms, currPlatforms)
            i += 1
        else:
            currPlatforms -= 1
            j += 1
    
    return platforms


if __name__ == '__main__':
    testCases = [
        ([900, 945, 955, 1100, 1500, 1800], [920, 1200, 1130, 1150, 1900, 2000])
    ]

    i = 0
    for arr, dep in testCases:
        print(f'TestCase {i}: {minPlatforms(arr, dep)}')
        i += 1