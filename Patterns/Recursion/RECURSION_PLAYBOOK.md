# 🌀 Recursion: The Playbook

This guide demystifies Recursion, breaking down its core logic, how to structure it in code, and the key patterns to identify in problems, turning complex challenges into manageable, self-similar steps.

-----

## 🧐 Concept

**Recursion** is a programming technique where a function calls itself to solve a problem. The core idea is to break down a large, complex problem into smaller, identical sub-problems until you reach a problem so simple it can be solved directly.

Think of it like a set of Russian nesting dolls. To open the whole set, you open the largest doll, which reveals a smaller, identical doll inside. You repeat this process—opening the "current" doll—until you reach the smallest, solid doll that can't be opened. That's your stopping point.

A recursive function always has two essential parts:

1.  **Base Case**: This is the simplest possible version of the problem, the "smallest doll." It's a condition that, when met, stops the recursion and returns a value directly without making another recursive call. Without a base case, a recursive function would call itself infinitely, leading to a "stack overflow" error.
2.  **Recursive Step**: This is where the function calls itself with a slightly modified input, bringing it closer to the base case. It's the rule that says, "To solve this problem, I first need to solve a smaller version of it."

<!-- end list -->

  * **Time Complexity**: Depends on the number of recursive calls and the work done in each call. It's often visualized as a "recursion tree."
  * **Space Complexity**: $O(m)$, where $m$ is the maximum depth of the recursion. Each function call adds a new layer to the call stack, consuming memory.

-----

## 💻 Implementation

Let's look at a classic example: calculating the factorial of a number, which is a great fit for your main language, Python.

### Generic Code (Factorial Example)

```python
def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.
    n! = n * (n-1) * (n-2) * ... * 1
    """
    # Base Case: The factorial of 0 or 1 is 1. This stops the recursion.
    if n == 0 or n == 1:
        return 1
    # Recursive Step: The problem is broken down into a smaller version.
    # The factorial of n is n multiplied by the factorial of (n-1).
    else:
        return n * factorial(n - 1)

```

### Example Dry Run

Let's trace how `factorial(4)` is computed.

  * **Goal**: Find the value of `4!`.

| Call Stack | `n` | Condition Met | Action | Return Value |
| :--- | :-: | :--- | :--- | :--- |
| `factorial(4)` | 4 | `n > 1` | `return 4 * factorial(3)` | `4 * 6 = 24` |
| ↳ `factorial(3)` | 3 | `n > 1` | `return 3 * factorial(2)` | `3 * 2 = 6` |
| ↳ ↳ `factorial(2)`| 2 | `n > 1` | `return 2 * factorial(1)` | `2 * 1 = 2` |
| ↳ ↳ ↳ `factorial(1)`| 1 | `n == 1` | `return 1` (Base Case) | `1` |

The calls build up until the base case is hit. Then, the results "unwind," with each function returning its value to the caller until the final result is computed.

-----

## 🕵️‍♂️ The Ultimate Cheat Sheet: How to Spot a Recursion Problem

Think "Recursion" when you see these characteristics in a problem.

1.  ### The Golden Rule: Self-Similar Subproblems

    Ask yourself: "**Can I solve this problem by first solving a smaller version of the exact same problem?**" If the solution for `N` can be expressed in terms of the solution for `N-1` or `N/2`, it's a prime candidate for recursion.

      * *Example*: Reversing a string `s`. The reverse of `"hello"` is `'o'` concatenated with the reverse of `"hell"`.

2.  ### The Tree/Graph/Nested Structure Pattern

    Problems involving data structures that are naturally recursive are almost always solved with recursion.

      * **Trees**: The definition is recursive (a tree is a root node with children that are also trees). Operations like finding height, traversing (in-order, pre-order, post-order), or searching for a node are classic recursion problems.
      * **Graphs**: Depth-First Search (DFS) is an inherently recursive algorithm for exploring a graph.
      * **Nested Lists/JSON**: Parsing or manipulating any hierarchical structure.

3.  ### The "Generate All of Something" Pattern (Backtracking)

    When a problem asks you to find **all possible** solutions, combinations, or permutations, it often requires exploring many different choices. Recursion is the natural way to implement this exploration, which is often called **backtracking**.

      * "Find all **subsets** of a set."
      * "Generate all valid **permutations**."
      * "Find all ways to place N-Queens on a chessboard."
      * The core idea is to make a choice, recurse to explore the consequences of that choice, and then "un-make" the choice (backtrack) to explore other options.

4.  ### The Divide and Conquer Pattern

    This is a specific type of recursion where you:

    1.  **Divide**: Break the problem into two or more smaller, independent sub-problems.
    2.  **Conquer**: Solve the sub-problems by making recursive calls.
    3.  **Combine**: Merge the results of the sub-problems to get the solution for the original problem.

    <!-- end list -->

      * *Classic Examples*: Merge Sort and Quick Sort.


5. ### The "Count the Ways" Pattern (Revised)

    This pattern is for problems asking "**How many ways** are there to do something?". The recursive function is designed to explore all possibilities and add up the number of successful outcomes.

    #### The `1` vs. `0` Base Case Logic

    A powerful way to frame these problems is to think of the base cases as follows:

    * **Return `1` (Success):** When the function reaches a state that represents one complete, valid solution. This tells the previous call, "We found one valid way from here\!"
    * **Return `0` (Failure/Dead End):** When the function reaches a state that is invalid or cannot lead to a solution (e.g., moving off a grid, breaking a rule). This tells the previous call, "This path leads to zero solutions."

    #### The Recursive Step

    The recursive step simply makes all possible next moves and **sums up their results**. This way, all the `1`s from the successful paths bubble up and get added together, giving you the total count.

    **Example: Counting Unique Paths in a Grid**

    Let's say we need to find the number of ways to get from the top-left corner `(0, 0)` to the bottom-right corner `(m, n)` of a grid, only moving right or down.

    ```python
    def count_paths(row, col, target_row, target_col):
        # Base Case (Failure): We've gone past the target. This path is invalid.
        if row > target_row or col > target_col:
            return 0

        # Base Case (Success): We've reached the target. This is one valid path.
        if row == target_row and col == target_col:
            return 1

        # Recursive Step: The total paths from here is the sum of paths
        # from moving down and paths from moving right.
        return count_paths(row + 1, col, target_row, target_col) + \
            count_paths(row, col + 1, target_row, target_col)

    # To start the process:
    # total_ways = count_paths(0, 0, m, n)
    ```

-----

## 🎯 Solved Problems

Here are some canonical problems that are best understood through the lens of recursion.

  * **Problem 1**: [Subsets](https://leetcode.com/problems/subsets/)

      * **Pattern**: A perfect example of the "Generate All of Something" pattern using backtracking. For each element, you explore two paths: one where you include the element in the subset and one where you don't.

  * **Problem 2**: [Permutations](https://leetcode.com/problems/permutations/)

      * **Pattern**: Another classic backtracking problem. You iterate through the numbers, pick one that hasn't been used, add it to the current permutation, and then recurse to find the rest of the permutation.

  * **Problem 3**: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

      * **Pattern**: A textbook case of the Tree/Nested Structure pattern. The depth of a tree is `1 + max(depth of left subtree, depth of right subtree)`.

  * **Problem 4**: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

      * **Pattern**: A counting problem that follows the "Self-Similar Subproblems" rule. The number of ways to reach step `n` is the sum of the ways to reach step `n-1` (by taking one step) and the ways to reach step `n-2` (by taking two steps).