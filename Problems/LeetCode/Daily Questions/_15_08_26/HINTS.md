# Intuition

At first, this problem looks like a subsequence/backtracking problem because we can either **pick** or **skip** every element.

That naturally leads to a recursive solution where we try all possible subsequences.

But there is a much simpler observation if we only care about the **XOR of the final subsequence**.

Let:

```python
total_xor = nums[0] ^ nums[1] ^ ... ^ nums[n-1]
```

There are only a few cases to consider.

### Case 1: The XOR of the entire array is non-zero

If:

```text
total_xor != 0
```

then we don't need to remove anything.

The entire array is already a valid subsequence, so the answer is simply:

```text
n
```

### Case 2: The XOR of the entire array is zero

Now the whole array is not valid.

Can we remove just one element?

Suppose we remove some non-zero element `x`.

The XOR of the remaining elements becomes:

```text
total_xor ^ x
```

Since `total_xor = 0`:

```text
0 ^ x = x
```

And because `x` is non-zero, the resulting XOR is also non-zero.

So, as long as the array contains **at least one non-zero element**, we can remove exactly one element and get a valid subsequence of length:

```text
n - 1
```

Note: If the array has at least one non-zero element and still the xor of whole array turned out to be 0, then it means there are more than 1 non-zero elements! So, we can confidently remove one non-zero element to get non-zero xor

### Case 3: Every element is zero

If every element is zero, then the XOR of every possible subsequence is also zero.

So there is no valid non-empty subsequence.

The answer is:

```text
0
```

That's it.

We don't actually need to generate subsequences at all.

---

# Approach

We just need to calculate two things while traversing the array:

1. The XOR of all elements.
2. Whether the array contains at least one non-zero element.

Then:

* If total XOR is non-zero → return `n`
* If total XOR is zero and there is a non-zero element → return `n - 1`
* Otherwise → return `0`

# Code

```python
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_nonzero = False

        for num in nums:
            total_xor ^= num

            if num != 0:
                has_nonzero = True

        if total_xor != 0:
            return len(nums)

        return len(nums) - 1 if has_nonzero else 0
```

# Complexity

* **Time:** `O(n)` — we traverse the array once.
* **Space:** `O(1)` — we only use a couple of variables.

# Why this is better than backtracking

The recursive solution tries different combinations of elements, which can lead to **O(2ⁿ)** possibilities.

The important trick here is realizing that we don't need to know *which* subsequence is optimal.

We only need to know:

> "Can I keep all `n` elements?"

If not:

> "Can I keep `n - 1` elements?"

And the XOR property tells us the answer immediately.

The key identity is:

```text
x ^ x = 0
x ^ 0 = x
```

That is what allows us to reduce the entire problem to a single pass through the array.
