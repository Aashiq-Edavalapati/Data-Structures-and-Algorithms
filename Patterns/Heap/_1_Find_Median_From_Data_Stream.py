# Link: https://leetcode.com/problems/find-median-from-data-stream/

"""
    @question(LC 295):
        The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

        For example, for arr = [2,3,4], the median is 3.
        For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
        Implement the MedianFinder class:

        MedianFinder() initializes the MedianFinder object.
        void addNum(int num) adds the integer num from the data stream to the data structure.
        double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
        
    ================================================================
    ================================================================
        
        Example 1:
            Input
                ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
                [[], [1], [2], [], [3], []]
            Output
                [null, null, null, 1.5, null, 2.0]

            Explanation
                MedianFinder medianFinder = new MedianFinder();
                medianFinder.addNum(1);    // arr = [1]
                medianFinder.addNum(2);    // arr = [1, 2]
                medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
                medianFinder.addNum(3);    // arr[1, 2, 3]
                medianFinder.findMedian(); // return 2.0
        
    ================================================================
    ================================================================

        Constraints:
            -105 <= num <= 105
            There will be at least one element in the data structure before calling findMedian.
            At most 5 * 104 calls will be made to addNum and findMedian.
"""
import heapq

"""
    @intuition:
        Since we are trying to find median, we need to keep the data stream sorted; and since we keep adding and querying simultaneously, we need to maintain the sorted order => Heap/Priority Queue

        But with a heap, we can only get first or last element in sorted stream, but we need middle element:
            Ex:- Consider the sorted stream [1, 3, 4, 5, 7, 8]:
                    - Now since we have even number elements => Median is (4 + 5) // 2
                        If we observe carefully, we can maintain left and right halves in sorted order separately:
                            Last element of 1st half and first element of 2nd half are middle elements
                    - If we have odd number of elements => Middle element should be an extra element, it should be present either in 1st or 2nd half only, let's consider it to be in 1st half.
                
                    From this we can see that the element from 1st half is max in that half and 2nd half is min:
                        Left half -> Max Heap
                        Right half -> Min Heap
                    
                    Another main observation is that we have to maintain a maximum difference of 1 in sizes of left and right halves
"""
class MedianFinder:
    
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        self.n = 0
    
    def addNum(self, num: int) -> None:
        # If left half is empty or num is smaller than left max => num should go into left half
        if not self.left_max_heap or -self.left_max_heap[0] > num:
            heapq.heappush(self.left_max_heap, -num)
            # IF size difference crosses 1, then shift an element
            if len(self.left_max_heap) > 1 + len(self.right_min_heap):
                heapq.heappush(self.right_min_heap, - heapq.heappop(self.left_max_heap))
        # Otherwise, num should go into the right half
        else:
            heapq.heappush(self.right_min_heap, num)
            # If right half has more size, shift an element
            if len(self.left_max_heap) < len(self.right_min_heap):
                heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))

        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 != 0:
            return -self.left_max_heap[0]
        return (self.right_min_heap[0] - self.left_max_heap[0]) / 2

if __name__ == '__main__':
    testCases = [
        (["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [[], [1], [2], [], [3], []]), # [null, null, null, 1.5, null, 2.0]
        (["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"], [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]), # [null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]
    ]

    for i, testCase in enumerate(testCases):
        ops, inps = testCase
        ans = [None]
        mf = MedianFinder()
        for op, inp in zip(ops[1:], inps[1:]):
            if op == "addNum":
                mf.addNum(inp[0])
                ans.append(None)
            else:
                ans.append(mf.findMedian())

        print(f"TestCase {i}:- \n\ti/p: operations={ops},\n\t     inputs={inps};\n\to/p: {ans}")