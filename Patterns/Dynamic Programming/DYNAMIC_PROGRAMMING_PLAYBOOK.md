# Dynamic Programming — The Playbook

This guide breaks down DP into its core patterns, templates, and mental models so you can recognize DP problems instantly and solve them systematically. It also includes the universal template for printing sequences and all major DP categories.

---

## 1. 4-Step Super Trick (Core DP Intuition)

### 1. Represent everything using **indexes**

Think in terms of:

* `i` (single index)
* `(i, j)` (pairs)
* `(i, j, k)` (triplets)
  These become your DP states.

### 2. Perform all problem actions on those indexes

Write all possible choices using indexes. This becomes your recurrence.

### 3. Combine results based on expectation

* **Count** → sum of choices
* **Max** → max of choices
* **Min** → min of choices

### 4. Add base cases

For counts: return `1` on success, `0` on failure.
For min/max: return direct base value.

This 4-step method forms the recursion.

---

## 2. Memoization (Top-Down)

### Steps

1. Create a `dp` array with dimensions matching your index representation. Initialize with `-1`.
2. Inside the recursive function:

   * After base cases → check `if dp[state] != -1: return dp[state]`.
3. Compute the answer, store in `dp[state]`, then return it.

Memoization = recursion + caching repeated subproblems.

---

## 3. Tabulation (Bottom-Up)

### Steps

1. Create a `dp` table of the required size.
2. Fill **base cases** just like recursion.
3. Iterate in the **reverse order** of recursion.
4. Copy recurrence and replace recursive calls like `f(i, j)` with `dp[i][j]`.

The final dp cell (like `dp[n][m]`) is the answer.

---

## 4. Space Optimization (For 2D+ DP)

When 2D DP only needs the previous row:

1. Use `prev` array instead of full 2D dp.
2. Fill base cases in `prev`.
3. For every outer loop:

   * Create `curr` array.
   * Replace `dp[i][j]` → `curr[j]`.
   * Replace `dp[i-1][j]` → `prev[j]`.
4. After inner loop → `prev = curr`.

This reduces space from O(n*m) → O(m).

---

## 5. Important Non-Intuitive Trick (Needed for Sequence Printing)

Fully space-optimized DP **cannot** reconstruct sequences because parent relations get lost.

For problems like:

* LIS printing
* LCS printing
* Path reconstruction
* Sequence of chosen items

You must:

* Keep a `parent[]` or `choice[][]` array, **or**
* Compute value using space-optimized DP, then re-run a second pass to trace choices.

For 90% of sequence-printing tasks, use normal DP + parent tracking.

---

## 6. Universal Template for Sequence Printing (DP + Parent)

Works for LIS, MSIS, chains, etc.

```
def build_sequence(arr, can_extend):
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n

    for i in range(n):
        for j in range(i):
            if can_extend(arr[j], arr[i]) and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    end = max(range(n), key=lambda x: dp[x])

    seq = []
    while end != -1:
        seq.append(arr[end])
        end = parent[end]

    seq.reverse()
    return seq
```

Rule: Whenever you update `dp[i]`, store `parent[i] = j`.

---

## 7. DP Pattern Index (Easy Classification)

### 1. Subset / Knapsack DP

Pick or skip. Decisions depend on capacity or constraints.

### 2. DP on Strings (2D DP)

LCS, edit distance, palindrome DP. State: `(i, j)`.

### 3. DP on Grids

Path sums, unique paths. State: `(i, j)`.

### 4. LIS-Style DP

State depends on previous elements. State: `i`.

### 5. DP with Printing

Use `parent[]` or `choice[][]`.

### 6. Digit DP

State: `(pos, tight, ... )`.

### 7. Bitmask DP

State represents subsets: `(mask, i)`.

### 8. Tree DP

Use DFS + DP on children.

### 9. Interval/Range DP

State: `(l, r)` — used in matrix chain multiplication.

---

## 8. Final Summary

1. Represent problem using indexes.
2. Write recursion with choices.
3. Use sum/min/max depending on requirement.
4. Add clear base cases.
5. Convert to memo → tabulation → space-opt.
6. For sequences: store parents.

This complete structure solves nearly every DP problem efficiently.