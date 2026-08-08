# Intuition

At first glance, this problem looks like a normal subsequence problem, but there is one annoying twist:

> We are allowed to change **at most one character** in the selected subsequence.

And on top of that, we don't just want *any* valid sequence — we want the **lexicographically smallest sequence of indices**.

So there are actually two things we need to think about:

* How do we decide **which indices to take**?
* When we encounter a mismatch, **when should we spend our one edit?**

The first part is fairly intuitive.

Since the answer is an array of indices and we want it lexicographically smallest, we should try to pick the **smallest possible index at every position**.

So while scanning `word1` from left to right:

* If `word1[i] == word2[j]`, we obviously want to take `i`.
* If they don't match, we have a decision:

  * Skip `i` and continue searching.
  * Or use our one edit at `i` and make `word1[i]` equal to `word2[j]`.

And this second case is where the actual problem lies.

If we use our edit too early, we might later discover that the remaining part of `word2` cannot be matched exactly.

So we need a way to answer:

> **"If I use my edit at the current index, can I match everything after it without using another edit?"**

That question leads to the main idea of the solution.

---

# Approach

The solution can be split into two passes.

### Pass 1: Process from right to left

We precompute information about how much of the **suffix of ****`word2`** can be matched exactly from every position in `word1`.

Let's call this array:

```python
suffixMatch[i]
```

The meaning of `suffixMatch[i]` is:

> Starting from `word1[i]`, how many characters from the **end of ****`word2`** can we match as a subsequence?

For example, if:

```text
word2 = "abcde"
```

and:

```text
suffixMatch[i] = 3
```

then the last 3 characters:

```text
"cde"
```

can be matched exactly somewhere inside:

```text
word1[i:]
```

The important part is that these characters are matched **in order**.

This is why a simple frequency array is not enough. We care about subsequence order, not just whether the characters exist.

---

### Pass 2: Greedily construct the answer

Now we scan `word1` from left to right.

Suppose we are currently trying to match:

```text
word2[j]
```

against:

```text
word1[i]
```

There are three possibilities.

### Case 1: Characters match

```python
word1[i] == word2[j]
```

Then we should take `i`.

Why?

Because `i` is the earliest index we have encountered that can provide the required character.

Taking a later index instead would only make the answer lexicographically larger.

So:

```python
seq.append(i)
j += 1
```

---

### Case 2: Characters don't match, but we still have our edit

Now we have:

```python
word1[i] != word2[j]
```

We could use our edit:

```text
word1[i] -> word2[j]
```

But we shouldn't blindly do that.

After using the edit, we need to match:

```text
word2[j + 1:]
```

**exactly**.

The length of this remaining part is:

```python
n - j - 1
```

And the remaining part of `word1` starts at:

```python
word1[i + 1:]
```

So we can safely use the edit if:

```python
suffixMatch[i + 1] >= n - j - 1
```

In other words:

> If the remaining suffix of `word2` can already be matched exactly from the remaining part of `word1`, then spending our edit here is safe.

And because `i` is the earliest possible index we're currently considering, taking it gives us the lexicographically smallest answer.

---

### Case 3: We cannot use the edit here

If:

```python
suffixMatch[i + 1] < n - j - 1
```

then using the edit at `i` would leave us unable to finish `word2`.

So we simply skip `i` and continue.

---

# Building `suffixMatch`

This is probably the most important part of the solution to understand.

We process `word1` from right to left.

At the same time, we keep a pointer `j` at the end of `word2`.

Whenever:

```python
word1[i] == word2[j]
```

we have successfully matched one more character from the end of `word2`.

So:

```python
suffixMatch[i] = suffixMatch[i + 1] + 1
```

and we move `j` backwards.

If the characters don't match, we simply skip `word1[i]`.

---

### Example

Consider:

```text
word1 = "bacdc"
word2 = "abc"
```

We want to understand what suffixes of `word2` can be matched exactly.

Starting from the end of `word2`:

```text
word2 = a b c
          ↑
```

We look for `'c'` from the right side of `word1`.

```text
word1 = b a c d c
              ↑
```

We find it.

Now we need `'b'`, so we continue moving left:

```text
word1 = b a c d c
        ↑
```

We find `'b'`.

Now there are no more characters needed for the suffix we're constructing.

So the suffix `"bc"` can be matched from the appropriate suffix of `word1`.

This gives us exactly the information we need later when deciding whether it is safe to spend our edit.

---

# Why Do We Need To Look From The Right?

This is the part that makes the whole solution click.

Suppose we're at a mismatch:

```text
word1[i] != word2[j]
```

and we're thinking:

> "Maybe I should use my edit here."

The only thing we care about after making that decision is:

```text
Can I finish the rest?
```

The rest is:

```text
word2[j + 1:]
```

And because we're not allowed to use another edit, this suffix has to be matched **exactly**.

So instead of repeatedly checking the entire suffix every time we encounter a mismatch, we preprocess that information once from right to left.

Then every decision becomes an `O(1)` lookup:

```python
suffixMatch[i + 1] >= n - j - 1
```

This is what keeps the whole algorithm linear.

---

# Why Is The Greedy Choice Correct?

There are two important greedy decisions here.

## 1. Always take an exact match

Suppose:

```python
word1[i] == word2[j]
```

Then we take `i`.

Why can't skipping `i` give us a better answer?

Because the answer is an array of indices.

If a valid answer can use some later index `k > i` for this position, then replacing `k` with `i` gives us:

```text
[i, ...]
```

instead of:

```text
[k, ...]
```

Since:

```text
i < k
```

the sequence using `i` is lexicographically smaller.

And taking an exact match doesn't consume our edit, so there is no downside.

Therefore:

> **If the current character matches, always take it.**

---

## 2. At a mismatch, use the edit as early as safely possible

This is the more interesting greedy choice.

Suppose:

```text
word1[i] != word2[j]
```

and we still haven't used our edit.

If we can change:

```text
word1[i] -> word2[j]
```

and still match the rest of `word2` exactly, then taking `i` is always better than skipping it.

Why?

Because skipping `i` means our first chosen index for this position will be some later index:

```text
k > i
```

So:

```text
[i, ...]
```

is lexicographically smaller than:

```text
[k, ...]
```

Therefore, we want to spend our edit at the **earliest position where doing so doesn't destroy feasibility**.

And `suffixMatch` tells us exactly whether doing that is safe.

---

# The Key Condition

This line:

```python
suffixMatch[i + 1] >= n - j - 1
```

is basically the entire decision-making part of the algorithm.

Let's break it down.

We are currently matching:

```text
word2[j]
```

and considering changing:

```text
word1[i] -> word2[j]
```

After that, we still need:

```text
word2[j + 1:]
```

Its length is:

```python
n - j - 1
```

And we will have to match all of those characters exactly from:

```text
word1[i + 1:]
```

`suffixMatch[i + 1]` tells us how many characters from the end of `word2` can be matched there.

Therefore:

```python
suffixMatch[i + 1] >= n - j - 1
```

means:

> "Yes, there is enough of the required suffix that can be matched exactly."

So we can safely spend our edit.

---

# Algorithm

1. Create `suffixMatch` of size `m + 1`.
2. Traverse `word1` from right to left.
3. Maintain a pointer at the end of `word2`.
4. Whenever the current characters match, increase the suffix match count and move the `word2` pointer backwards.
5. Traverse `word1` again from left to right.
6. If `word1[i] == word2[j]`, take index `i`.
7. Otherwise, if the edit hasn't been used and the remaining suffix can be matched exactly, take `i` and mark the edit as used.
8. Otherwise, skip `i`.
9. If we collect exactly `len(word2)` indices, return them.
10. Otherwise, return an empty array.

---

# Code

```python
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)

        # suffixMatch[i] tells us how many characters
        # from the end of word2 can be matched exactly
        # inside word1[i:].
        suffixMatch = [0] * (m + 1)

        j = n - 1

        # Build suffixMatch from right to left.
        for i in range(m - 1, -1, -1):
            suffixMatch[i] = suffixMatch[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                suffixMatch[i] += 1
                j -= 1

        seq = []
        i = j = 0
        edited = False

        # Greedily construct the lexicographically
        # smallest sequence.
        while i < m and j < n:

            # Case 1: Exact match.
            if word1[i] == word2[j]:
                seq.append(i)
                j += 1

            # Case 2: Use our one edit if doing so
            # still allows the rest of word2 to be
            # matched exactly.
            elif not edited and suffixMatch[i + 1] >= n - j - 1:
                seq.append(i)
                edited = True
                j += 1

            # Otherwise, skip word1[i].
            i += 1

        return seq if len(seq) == n else []
```

![upvote_cat.png](https://assets.leetcode.com/users/images/60e744d1-e62c-44a2-8357-7ff1280767fa_1784461458.718262.png)

---

# Dry Run

Let's take:

```text
word1 = "bacdc"
word2 = "abc"
```

We want three indices.

Initially:

```text
i = 0
j = 0
edited = False
seq = []
```

So we're looking for:

```text
word2[0] = 'a'
```

---

### `i = 0`

```text
word1[0] = 'b'
word2[0] = 'a'
```

Mismatch.

Can we use our edit here?

If we do:

```text
b -> a
```

we still need:

```text
"bc"
```

afterwards.

But the remaining part of `word1` is:

```text
"acdc"
```

There isn't a `'b'` there.

So this edit is unsafe.

We skip index `0`.

```text
seq = []
```

---

### `i = 1`

Now:

```text
word1[1] = 'a'
word2[0] = 'a'
```

Exact match!

Take it:

```text
seq = [1]
j = 1
```

Now we need:

```text
word2[1] = 'b'
```

---

### `i = 2`

```text
word1[2] = 'c'
word2[1] = 'b'
```

Mismatch.

This time, suppose we use our edit:

```text
c -> b
```

After that we need:

```text
"c"
```

from the remaining part:

```text
"dc"
```

That's possible.

So we take index `2`:

```text
seq = [1, 2]
edited = True
j = 2
```

---

### `i = 3`

```text
word1[3] = 'd'
word2[2] = 'c'
```

We already used our edit, so we cannot change `d`.

Skip it.

---

### `i = 4`

```text
word1[4] = 'c'
word2[2] = 'c'
```

Exact match.

Take it:

```text
seq = [1, 2, 4]
```

We have matched all of `word2`.

Therefore:

```text
[1, 2, 4]
```

is returned.

---

# Why Not Just Use The Edit At The First Mismatch?

This is a very tempting approach, but it doesn't work.

Consider:

```text
word1 = "bacdc"
word2 = "abc"
```

At index `0`:

```text
b != a
```

It is tempting to say:

```text
"Great, use our edit here."
```

But doing:

```text
b -> a
```

would leave us needing:

```text
"bc"
```

from:

```text
"acdc"
```

There is no `'b'` left.

So we would have wasted our only edit and eventually fail.

The important lesson is:

> **The earliest mismatch is not necessarily the earliest place where we can spend the edit.**

Instead, we want:

> **The earliest mismatch where spending the edit is still feasible.**

That's exactly what `suffixMatch` helps us determine.

---

# Why Not Use Frequency Counts?

Initially, it might seem like we could store the frequency of every character to the right and use that to determine whether the suffix is possible.

But frequency alone isn't enough.

Suppose we need:

```text
"abc"
```

and the remaining part of `word1` is:

```text
"cba"
```

The frequencies are perfect:

```text
a -> 1
b -> 1
c -> 1
```

But `"abc"` is **not** a subsequence of `"cba"`.

The order is wrong.

That's why we don't store character frequencies.

Instead, we directly compute how much of the **required suffix of ****`word2`** can be matched in order.

---

# Complexity

Let:

```text
m = len(word1)
n = len(word2)
```

### Time Complexity

We traverse `word1` twice:

* Once from right to left.
* Once from left to right.

Both passes are `O(m)`.

Therefore:

```text
O(m)
```

The `word2` pointer only moves backwards/forwards and never causes another nested scan.

So the overall time complexity is:

```text
O(m + n)
```

which is effectively linear in the input size.

### Space Complexity

We store:

```python
suffixMatch
```

which has `m + 1` elements.

The answer itself contains at most `n` indices.

So the auxiliary space is:

```text
O(m)
```

excluding the output.

---

# Final Takeaway

The problem looks difficult mainly because of this one decision:

> **At a mismatch, should I spend my one edit here or skip this index?**

Once we phrase the question correctly, the solution becomes much simpler.

We don't need to try both possibilities.

Instead, we ask:

```text
"If I use the edit here,
 can I match everything remaining exactly?"
```

To answer that efficiently, we preprocess the string from right to left using `suffixMatch`.

Then the actual greedy scan is straightforward:

```text
Exact match?
    ↓
Take it.

Mismatch + edit is safe?
    ↓
Take it and spend the edit.

Otherwise
    ↓
Skip it.
```

The nice part is that we're always making the **earliest feasible choice**, which is exactly what we want when the answer itself is an array of indices and we want it to be lexicographically smallest.

And that's what gets us an `O(m + n)` solution.
