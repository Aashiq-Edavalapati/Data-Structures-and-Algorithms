# 🧠 Greedy Algorithms: The Playbook

Welcome to the playbook for **Greedy Algorithms**. This powerful strategy solves problems by making the most obvious and optimal choice at every single step, without worrying about the future.

---

## 🧐 Concept: The Core Idea

At its heart, **Greedy** is about making the **best local choice** at every step, hoping it leads to a **globally optimal solution**.

Unlike dynamic programming (which explores multiple states), Greedy commits early. The trick is: **Greedy only works when the problem has a certain structure (*optimal substructure* + *greedy-choice property*)**.

- **Optimal Substructure**: The global solution can be built by combining optimal solutions to subproblems.
- **Greedy Choice Property**: At each step, a locally optimal choice will eventually lead to a global optimum.

A **Greedy Algorithm** builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. It's a "live in the moment" strategy.

Think of making change with standard US coins (1, 5, 10, 25 cents). To give back 49 cents, you greedily take the largest coin possible without going over:

1.  Take a **quarter** (25). Remaining: 24.
2.  Can't take another quarter. Take a **dime** (10). Remaining: 14.
3.  Take another **dime** (10). Remaining: 4.
4.  Take four **pennies** (1). Remaining: 0.

You never second-guess your choices. You just keep taking the best immediate option.

### **⚠️ The Big Warning: When Greed Fails**

Greedy algorithms don't always work\! They fail if a locally optimal choice can lead to a globally suboptimal outcome. If the coin system was `{1, 7, 10}` and you needed to make change for `14`, the greedy choice would be `10 + 1 + 1 + 1 + 1` (5 coins), while the optimal solution is `7 + 7` (2 coins). Always be sure to validate the "No Regrets" test\!

-----

### 🔑 Core Intuition

Greedy = "What’s the most obvious **best move right now**?"

* If this move **never causes regrets later**, Greedy works.
* If it can block a better future choice → Greedy fails (and you need DP).

---

## 💻 Generic Implementation Template

There isn't one template for greedy code, but there is a common **thought process**:

1.  **Identify the Greedy Choice**: What criterion defines the "best" move? (e.g., earliest finish time, highest value/weight ratio).
2.  **Sort**: Sort the input data based on your greedy criterion.
3.  **Iterate and Build**: Loop through the sorted data, building the solution step-by-step. At each step, make the greedy choice if it's valid.

```python
def greedy_solve(items):
    # Step 1: Sort (common in greedy problems)
    items.sort(key=lambda x: criterion(x))

    result = []
    for item in items:
        if can_choose(item, result):
            result.append(item)

    return result
```

* **criterion** = the greedy key (end time, ratio, weight, distance…).
* **can\_choose** = feasibility test (no overlap, within capacity, etc).

---

## 🕵️‍♂️ The Ultimate Cheat Sheet: How to Spot a Greedy Problem

If a problem has these characteristics, a Greedy approach should be the first thing you consider.

### 1. The Core Question: Optimization

Nearly all greedy problems ask for an **optimal** value—either the **MAXIMUM** or **MINIMUM** of something.

* "Find the **minimum** number of coins..."
* "Find the **maximum** profit..."
* "Find the **minimum** number of platforms required..."
* "Find the **maximum** number of activities you can attend..."
    
⚠️ DP problems also ask this — so you need more signals.

### 2. The "Best Choice Now" Heuristic

The problem can be solved by making a sequence of choices. At each step, one choice looks **unambiguously better** than all others based on some simple rule. You make that choice and move on without ever reconsidering. 

Ask yourself: "What is the most obvious 'best' move I can make *right now*?"

* **Example (Activity Selection):** The "best" choice is to pick the activity that **finishes earliest**, as it frees up your time for other potential activities sooner than any other choice.

### 3. Sorting is the Key

Most greedy solutions become simple after **sorting**.

* By end time → Interval scheduling.
* By value/weight ratio → Fractional Knapsack.
* By deadline → Job sequencing.

Sorting reveals the greedy criterion.

### 4. The "No Regrets" Test (The Greedy Choice Property)

    This is the most critical test.

Ask: *If I commit to this choice, will I regret it later?*

* ✅ Coin Change (canonical denominations): Taking a quarter first never blocks optimality.
* ❌ 0/1 Knapsack: Picking the highest-value item first can ruin the optimal solution.

If **no regrets** → Greedy is correct.

-----

### 5. The "Discard Half / Range-Carrying" Pattern

Instead of recursion or DP, you **carry ranges** forward greedily.

* Maintain `(min, max)` validity or `(left, right)` intervals.
* Expand the range step by step with the best extension.

**Examples:**

* **Valid Parenthesis with Wildcards** (`(*))` problem): Track `min` and `max` open counts.
* **Jump Game II**: Maintain a `[l, r]` window of reachable indices, then greedily extend `r` to the farthest jump.

```python
# Parenthesis validity greedy range
min_open, max_open = 0, 0
for ch in s:
    if ch == '(':
        min_open += 1; max_open += 1
    elif ch == ')':
        min_open -= 1; max_open -= 1
    else:  # wildcard
        min_open -= 1; max_open += 1
    if min_open < 0: min_open = 0
    if max_open < 0: return False
return min_open == 0
```

---

### 6. The "Greedy by Ratio" Pattern

Pick by **efficiency** (per unit measure).

* Fractional Knapsack → maximize value/weight.
* Huffman Coding → merge two smallest frequencies.

---

### 7. The "Extreme First" Pattern

Always pick the **largest** or **smallest** first.

* Coin Change (largest denomination first).
* Rope Joining → always join smallest ropes first.
* Huffman → pick 2 smallest each time.

---

### 8. The "Covering / Dominating" Pattern

You must **cover ranges/points** with minimum resources.

* Burst Balloons → minimum arrows.
* Minimum Platforms → overlapping intervals.

---

### 9. The "Greedy + Heap" Pattern

If choices evolve dynamically, use a **priority queue**.

* Course Schedule III → drop longest courses if exceeding time.
* Meeting Rooms II → min heap of end times.

---

## 🎯 Solved Problems: See It in Action

  * **Problem 1**: [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

      * **Pattern**: Sort by start time. Greedily merge the current interval with the next one if they overlap.

  * **Problem 2**: [Fractional Knapsack](https://www.geeksforgeeks.org/fractional-knapsack-problem/)

      * **Pattern**: Sort items by value-to-weight ratio. Greedily pick the items with the highest ratio until the knapsack is full.

  * **Problem 3**: [Gas Station](https://leetcode.com/problems/gas-station/)

      * **Pattern**: A clever greedy proof. If the total gas is more than the total cost, a solution exists. The starting point is the station right after the "worst" negative-gain segment.

  * **Problem 4**: [Jump Game](https://leetcode.com/problems/jump-game/)

      * **Pattern**: At each position, greedily jump to the position that extends your reach the furthest. Keep track of the maximum reachable index
    
---

# 🔥 **Key Takeaway**:
If the problem screams **optimization**, you feel the urge to **sort**, and making the **obvious best choice now** never blocks global optimality → it’s Greedy.
If in doubt, test with the **No Regrets Rule** or **Exchange Argument**.