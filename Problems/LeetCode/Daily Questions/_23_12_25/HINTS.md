### The General Rule of Thumb

When dealing with interval problems (segments with a start and end):

#### 1. Maximizing the **COUNT** (Greedy Strategy)

* **The Goal:** Fit as many items as possible into the container/timeline.
* **The Pattern:** **Sort by End Point (Ascending).**
* **Why:** The "Greedy Choice Property." By picking the item that finishes earliest, you leave the maximum possible room for subsequent items. You don't care about the "quality" or "value" of the item, only that it "finishes quick" so you can pick another one.
* **Algorithm:**
1. Sort by End `[start, END, val]`.
2. Iterate and pick the first non-overlapping item.
3. Complexity: .



#### 2. Maximizing the **VALUE / WEIGHT** (Dynamic Programming / Search)

* **The Goal:** Get the highest total profit, weight, or score, even if it means picking fewer items.
* **The Pattern:** **Sort by Start Point (Ascending).**
* **Why:** A short, quick event might have a value of 1, while a long event might have a value of 100. Greedy (sorting by end) fails here because it would pick the short cheap one and block the long valuable one.
* Sorting by Start Time organizes the timeline so you can process decisions linearly: *"If I pick this item starting at , what is the best I can do with the remaining timeline starting after ?"*


* **Algorithm:**
1. Sort by Start `[START, end, val]`.
2. Use Binary Search (to jump to the next valid start time) combined with Suffix Max Arrays (for fixed K steps) or Dynamic Programming (for general K steps).
3. Complexity: .



---

### Comparison Table for Interviews

You can memorize this mental model:

| Feature | **"Greedy" Scenarios** | **"Weighted" Scenarios** |
| --- | --- | --- |
| **Objective** | Maximize **Quantity** (Count) | Maximize **Quality** (Sum/Profit) |
| **Typical Phrasing** | "Max number of meetings", "Max non-overlapping intervals" | "Max profit", "Max score", "Max sum", "Weighted Interval Scheduling" |
| **Sorting Key** | **End Time** (Ascending) | **Start Time** (Ascending) |
| **Key logic** | *"Finish fast to leave room for others."* | *"Check this item + the best future option."* |
| **Technique** | Simple Loop | Binary Search + DP/Memoization |

### Real-world "Non-Time" Examples

This pattern applies to anything with a "Start" and "End" constraint:

1. **Memory Management:** You have a linear block of RAM. Processes request address ranges `[0x100, 0x500]`.
* *Max processes?* Sort by End Address.
* *Max priority processes?* Sort by Start Address.


2. **Logistics/Cargo:** You have a long truck bed. Boxes take up space from meter `x` to meter `y`.
* *Max number of boxes?* Sort by End Position.
* *Max value of cargo?* Sort by Start Position.


3. **DNA Sequencing:** You have fragments of DNA mapping to indices `i` to `j` on a chromosome.
* *Max number of non-overlapping gene fragments?* Sort by End Index.



### A Small Caveat (DP with End Sort)

Technically, you *can* solve the "Max Value" problem by sorting by End Time using Dynamic Programming, but it is often conceptually harder to implement during an interview (requires finding the "previous" non-overlapping interval).

**Recommendation:** Stick to the **Start Time Sort + Binary Search** pattern for Max Value problems. It is more standard, easier to debug, and applies cleanly to "Top-Down" recursion logic which is intuitive to explain in interviews.