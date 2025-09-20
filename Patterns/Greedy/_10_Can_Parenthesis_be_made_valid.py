def helperBruteForce(s, ind, cnt):
    if cnt < 0:
        return False
    
    if ind == len(s):
        return cnt == 0
    
    if s[ind] == '(':
        return helperBruteForce(s, ind + 1, cnt + 1)
    elif s[ind] == ')':
        return helperBruteForce(s, ind + 1, cnt - 1)
    
    return helperBruteForce(s, ind + 1, cnt + 1) or helperBruteForce(s, ind + 1, cnt - 1) or helperBruteForce(s, ind + 1, cnt)

def canParenthesize(s):
    # return helperGreedy(s, 0, 0) # Brute Force
    min, max = 0, 0
    for char in s:
        if char == '(':
            min += 1
            max += 1
        elif char == ')':
            min -= 1
            max -= 1
        else:
            min -= 1
            max += 1
        if min < 0: min = 0
        if max < 0: return False
    
    return min == 0

if __name__ == '__main__':
    testCases = [
        "(()())", # True
        "(*)",    # True
        "(*))",   # True
        "(**(",   # False
        "()*)*(", # False
        "()*)*(*",# True
        "()*)*()",# True
    ]

    i = 0
    for s in testCases:
        print(f'TestCase {i}: {canParenthesize(s)}')
        i += 1