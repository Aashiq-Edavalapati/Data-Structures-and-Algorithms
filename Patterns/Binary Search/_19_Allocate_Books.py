# -----------------------------------------------------------------------------
# Problem: Allocate Books
# -----------------------------------------------------------------------------
#
# @question:
#   You are given an array `arr` where arr[i] is the number of pages in the i-th book,
#   and an integer `students` which is the number of students.
#   You must allocate books in order (no rearranging), so that each student
#   gets at least one book, and the maximum number of pages assigned
#   to any student is as small as possible.
#
#   Return the minimum possible value of the maximum pages a student has to read.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
#   - We are not searching inside the array, but for the "minimum maximum pages".
#   - Monotonicity: If books can be allocated with `maxPages` limit,
#     then any larger limit also works. If it cannot be done with `maxPages`,
#     then any smaller limit also fails.
#   - This monotonic property allows us to apply binary search.
#
# -----------------------------------------------------------------------------
# @method (easy steps):
#   1. Minimum possible pages = max(arr), because one student must read
#      at least the thickest book.
#   2. Maximum possible pages = sum(arr), if only one student gets all the books.
#   3. Binary search between [max(arr), sum(arr)]:
#       - For a mid value, check how many students are needed
#         if no student is allowed to read more than `mid` pages.
#       - If the number of students needed > given students → increase `left`.
#       - Otherwise, move `right` down to try smaller maximum pages.
#   4. At the end, `left` gives the smallest possible maximum pages.
#
# Time Complexity: O(N log(sum(arr) - max(arr)))
# Space Complexity: O(1)
# ==============================================================================

def canBeAllocated(arr, maxPages):
    """
    Return how many students are needed if each student
    cannot read more than `maxPages`.
    """
    i = 1
    currPages = arr[0]   # pages assigned to current student
    students = 1         # start with first student
    
    while i < len(arr):
        # If adding this book exceeds limit, assign to new student
        if currPages + arr[i] > maxPages:
            currPages = arr[i]
            students += 1
            i += 1
            continue
        
        # Otherwise, keep assigning books to current student
        currPages += arr[i]
        i += 1
    
    return students

def minMaxPages(arr, students):
    """
    Find the minimum possible maximum pages any student has to read.
    """
    left, right = max(arr), sum(arr)

    while left <= right:
        mid = left + (right - left) // 2

        # If more students are required, mid is too small
        if canBeAllocated(arr, mid) > students:
            left = mid + 1
        else:
            # Otherwise, mid may be the answer, but try smaller
            right = mid - 1
    
    # The first valid capacity is at `left`
    return left

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([25, 46, 28, 49, 24], 4)
    ]

    i = 0
    for arr, students in testCases:
        print(f'TestCase {i}: {minMaxPages(arr, students)}')
        i += 1
