# 🧠 Binary Search: The Playbook

This guide breaks down Binary Search, explaining its core idea, implementation, and the key patterns to look for in problems so you can master this fundamental algorithm.

---

## 🧐 Concept

At its heart, **Binary Search** is a highly efficient algorithm for finding an item from a **sorted** collection of items.

Think of it like searching for a word in a physical dictionary. You don't check every page from the beginning. Instead, you open to the middle, see if your word comes before or after the words on that page, and then discard half the dictionary. You repeat this, halving the search space each time until you find the word.

**Key Idea**: The core principle is to repeatedly divide the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half.

* **Time Complexity**: $O(\log n)$ - because we discard half of the search space with each comparison.
* **Space Complexity**: $O(1)$ for the iterative version (which is generally preferred).

---

## 💻 Implementation

Here’s a standard implementation in Python, your preferred language.

### Generic Code

```python
# [Path in repo: ./Binary_Search/binary_search.py]

def binary_search(arr, target):
    """
    A standard iterative implementation of Binary Search.
    Finds the index of 'target' in a sorted 'arr'.
    Returns -1 if the target is not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Use left + (right - left) // 2 to prevent potential integer overflow
        # in languages with fixed-size integers.
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Target found!
            return mid
        elif arr[mid] < target:
            # The target must be in the right half of the remaining array.
            left = mid + 1
        else:
            # The target must be in the left half of the remaining array.
            right = mid - 1

    # Target was not found in the array.
    return -1
````

### Example Dry Run

Let's trace the algorithm with a simple example.

  * **Input**: `arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]`, `target = 23`
  * **Goal**: Find the index of `23`.

| Iteration | `left` | `right` | `mid` | `arr[mid]` | Condition Met      | Action                                   |
| :-------- | :----: | :-----: | :---: | :--------: | :----------------- | :--------------------------------------- |
| 1         | 0      | 8       | 4     | 16         | `16 < 23`          | Search right half. Set `left = mid + 1`  |
| 2         | 5      | 8       | 6     | 38         | `38 > 23`          | Search left half. Set `right = mid - 1` |
| 3         | 5      | 5       | 5     | 23         | `23 == 23`         | **Target found\!** Return `mid`.          |

  * **Output**: `5`

### ▶️ Experiment with the Code\!

To see it in action, you can explore and run the implementation file directly.

**[🧑‍💻 Run the Python implementation\!](./implementation/00_binarySearch.py)**

-----

## 🕵️‍♂️ The Ultimate Cheat Sheet: How to Spot a Binary Search Problem

This is the core of the playbook. If a problem contains any of these clues, your first thought should be Binary Search.

1. ### The Golden Rule: Search Space is Sorted or Monotonic

    The most obvious clue is a **sorted array**. If you're given one and asked to find something, it's almost certainly Binary Search. But it's not just about arrays! The *concept* of the search space can be sorted. For example, you might be searching for an answer within a range of numbers (e.g., `1` to `1,000,000,000`), where the validity of the answer is monotonic.

2. ### The "Binary Search on Answer" Pattern
    This is the most common and powerful variant. You can use it when the problem asks you to find the **MINIMUM** or **MAXIMUM** value of something that satisfies a condition.
    * "Find the **minimum time** to..."
    * "Find the **maximum capacity** that..."
    * "Find the **smallest number** such that..."
    * The key insight: You can create a function, `can_solve(k)`, that checks if it's possible to solve the problem with a value of `k`. This function will have a monotonic property (e.g., `False, False, ..., True, True, True...`). You binary search on the value `k` to find the first `True` (for minimization) or the last `True` (for maximization).

3. ### The "Discard Half" Test
    Ask yourself this question: "If I pick a random value from my search space, can I definitively **eliminate half** of the remaining possibilities?" If the answer is yes, it’s a Binary Search problem. This applies even in seemingly unsorted arrays, like in the "Find Peak Element" problem.

-----

## 🎯 Solved Problems

Applying the theory is the best way to learn. Here are some problems solved using Binary Search that highlight its common patterns.

  * **Problem 1**: [Search a 2D Matrix](https://www.google.com/search?q=./Solved_Problems/search-a-2d-matrix.md)

      * **Pattern**: Applying standard Binary Search on a conceptual 1D array mapped from a 2D matrix.

  * **Problem 2**: [Find First and Last Position of Element in Sorted Array](https://www.google.com/search?q=./Solved_Problems/find-first-and-last-position.md)

      * **Pattern**: A classic modification of Binary Search on a sorted array to find boundaries, not just the element itself. Requires two separate binary searches.

  * **Problem 3**: [Koko Eating Bananas](https://www.google.com/search?q=./Solved_Problems/koko-eating-bananas.md)

      * **Pattern**: A perfect example of "Binary Search on Answer." The goal is to find the *minimum eating speed `k`* (the answer) that allows Koko to eat all bananas within `H` hours.

  * **Problem 4**: [Find Peak Element](https://www.google.com/search?q=./Solved_Problems/find-peak-element.md)

      * **Pattern**: Searching in an unsorted array, but the properties of a "peak" guarantee that you can always discard half the elements at each step.