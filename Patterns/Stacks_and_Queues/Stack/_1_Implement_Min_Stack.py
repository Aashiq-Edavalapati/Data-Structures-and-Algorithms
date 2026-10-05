# Link: https://leetcode.com/problems/min-stack

"""
    @question:
        Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        Implement the MinStack class:

        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
        You must implement a solution with O(1) time complexity for each function.

    ----------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------        

        Example 1:
            Input:        ["MinStack","push","push","push","getMin","pop","top","getMin"]
                        [[],[-2],[0],[-3],[],[],[],[]]

            Output:         [null,null,null,null,-3,null,0,-2]

            Explanation:
                MinStack minStack = new MinStack();
                minStack.push(-2);
                minStack.push(0);
                minStack.push(-3);
                minStack.getMin(); // return -3
                minStack.pop();
                minStack.top();    // return 0
                minStack.getMin(); // return -2
        
    ----------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------

        Constraints:
            -231 <= val <= 231 - 1
            Methods pop, top and getMin operations will always be called on non-empty stacks.
            At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class Node:
    
    def __init__(self, val, next_, prev):
        self.val = val
        self.next = next_
        self.prev = prev

class MinStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:
        if not self.head:
            node = Node((val, val), None, None)
            self.head = node
            self.tail = node
            return

        node = Node((val, min(val, self.tail.val[1] if self.tail else val)), None, self.tail)
        if self.tail: self.tail.next = node
        self.tail = node

    def pop(self) -> None:
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

    def top(self) -> int:
        return self.tail.val[0]

    def getMin(self) -> int:
        return self.tail.val[1]


# MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
if __name__ == '__main__':
    testCases = [
        (
            ["MinStack","push","push","push","getMin","pop","top","getMin"],
            [[],[-2],[0],[-3],[],[],[],[]]
        ),
        (
            ["MinStack","push","push","push","getMin","pop","getMin","pop","getMin","pop","push","push","push","getMin","pop","top","getMin","pop","getMin","pop"], 
            [[],[0],[1],[0],[],[],[],[],[],[],[-2],[-1],[-2],[],[],[],[],[],[],[]] 
        )
    ]

    obj = None
    outputs = []

    for i, testCase in enumerate(testCases):
        commands, inputs = testCase
        for cmd, val in zip(commands, inputs):
            if cmd == "MinStack":
                obj = MinStack()
                outputs.append(None)

            elif cmd == "push":
                obj.push(val[0])
                outputs.append(None)

            elif cmd == "pop":
                obj.pop()
                outputs.append(None)

            elif cmd == "top":
                outputs.append(obj.top())

            elif cmd == "getMin":
                outputs.append(obj.getMin())

        print(f"\n======= Test Case {i} =======")

        for step, (cmd, val, out) in enumerate(zip(commands, inputs, outputs)):
            print(f"Step {step:02d}:")
            print(f"   Command : {cmd}")
            print(f"   Input   : {val}")
            print(f"   Output  : {out}")
            print()

        print("==============================\n")

