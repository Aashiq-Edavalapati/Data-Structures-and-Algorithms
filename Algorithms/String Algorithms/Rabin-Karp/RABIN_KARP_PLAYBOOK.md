# Rabin–Karp String Matching — Playbook

Rabin–Karp is another algorithm for **finding a pattern inside a text**.

At first, it might sound similar to KMP because they solve a similar problem, but their thinking is completely different.

KMP says:

> **"I already matched this structure, so let me reuse it."**

Rabin–Karp says:

> **"Instead of comparing every character, let me compare fingerprints of the strings."**

That fingerprint is called a **hash**.

Once you understand the idea of a **rolling hash**, the rest of Rabin–Karp becomes pretty straightforward.

---

# 1. What problem does Rabin–Karp solve?

The classic problem is:

> **Find where a pattern occurs inside a text.**

For example:

```text
Text:    ABABDABABABABCABAB
Pattern: ABAB
```

We want:

```text
[0, 5, 7, 15]
```

The naive approach checks the pattern character-by-character at every possible position.

Rabin–Karp tries to make this faster by assigning a numeric **hash** to the pattern and to every substring of the text having the same length.

Instead of immediately asking:

```text
"Are these 4 characters equal?"
```

we first ask:

```text
"Do their hashes match?"
```

If the hashes are different, they definitely aren't equal.

If the hashes match, we verify the actual strings.

---

# 2. The main idea in one sentence

If you remember only one thing from this playbook:

> **Rabin–Karp uses a rolling hash to quickly compare the pattern with every same-sized window of the text.**

That's the whole algorithm in a nutshell.

---

# 3. Why not just compare strings directly?

Suppose:

```text
Text:    A B C D E F G H
Pattern: C D E
```

We can look at every window:

```text
A B C
B C D
C D E  ← match
D E F
E F G
F G H
```

With direct comparison, we'd potentially inspect several characters for every window.

Instead, Rabin–Karp gives each window a hash:

```text
ABC → hash
BCD → hash
CDE → hash
DEF → hash
EFG → hash
FGH → hash
```

The pattern also gets a hash:

```text
CDE → hash
```

Now we can quickly compare:

```text
hash(pattern) == hash(window)
```

Most windows can be rejected immediately.

---

# 4. But how do we calculate all those hashes efficiently?

This is where the **rolling hash** comes in.

Suppose our window is:

```text
ABCD
```

and we move one position to the right:

```text
BCDE
```

We don't want to calculate the hash of `BCDE` completely from scratch.

We already know the hash of:

```text
ABCD
```

So we:

```text
1. Remove A
2. Shift the remaining value
3. Add E
```

That's why it's called a:

> **Rolling hash**

The hash basically "slides" along with the window.

---

# 5. Think of it like a sliding window

This is probably the easiest way to visualize Rabin–Karp.

Suppose:

```text
Text = ABCDEFG
Pattern = CDE
```

The window size is `3`.

We slide it across the text:

```text
[A B C] D E F G
  ↓
  hash = ...

A [B C D] E F G
    ↓
    hash = ...

A B [C D E] F G
      ↓
      hash = ...

A B C [D E F] G
        ↓
        hash = ...

A B C D [E F G]
          ↓
          hash = ...
```

At each position:

```text
window hash == pattern hash ?
```

If no:

```text
Definitely not a match.
```

If yes:

```text
Maybe a match.
Verify the actual substring.
```

---

# 6. Why do we need to verify the string?

This is one of the most important differences between Rabin–Karp and KMP.

Two different strings can theoretically have the same hash.

For example:

```text
ABC → hash = 123
XYZ → hash = 123
```

This is called a **hash collision**.

So:

```text
Same hash
   ↓
Maybe equal
   ↓
Compare actual strings
```

But:

```text
Different hash
   ↓
Definitely different
```

Therefore, a proper Rabin–Karp implementation does:

```python
if pattern_hash == window_hash:
    if text[i:i + m] == pattern:
        found.append(i)
```

The hash gets us to a **candidate match** quickly, and the actual comparison confirms it.

---

# 7. How is a string converted into a hash?

We can treat the characters like numbers.

For example:

```text
A → 65
B → 66
C → 67
```

A simple polynomial-style hash can look like:

```text
hash("ABC")

= ((65 × base + 66) × base + 67)
```

Usually we calculate everything modulo a large number:

```text
hash = hash % mod
```

This keeps the numbers manageable.

A typical implementation uses values like:

```python
base = 256
mod = 10**9 + 7
```

You don't need to memorize these exact values.

The important idea is:

> **Characters contribute to the hash based on their position.**

---

# 8. The rolling hash formula

Suppose our current window is:

```text
ABCD
```

and we want to move to:

```text
BCDE
```

The old hash contains:

```text
A × base³
B × base²
C × base
D
```

First remove:

```text
A × base³
```

Then multiply the remaining value by `base`:

```text
B × base²
C × base
D
```

becomes:

```text
B × base³
C × base²
D × base
```

Then add the new character:

```text
E
```

So the new window becomes:

```text
B × base³
C × base²
D × base
E
```

which is exactly the hash of:

```text
BCDE
```

That's the rolling part.

---

# 9. What is `high` in the code?

You'll usually see something like:

```python
high = pow(base, m - 1, mod)
```

This represents:

```text
base^(m - 1)
```

Why do we need it?

Because we need to remove the **leftmost character** from the current window.

For a window of length `4`:

```text
A B C D
↑
```

`A` contributes:

```text
A × base³
```

So we need:

```text
base³
```

to remove its contribution.

That's exactly what `high` stores.

You can think of it as:

> **The multiplier attached to the leftmost character of the window.**

---

# 10. Moving the window

Suppose:

```text
window = ABCD
```

and we're moving to:

```text
BCDE
```

The code conceptually does:

```python
# Remove A
window_hash -= ord('A') * high

# Shift the remaining characters
window_hash *= base

# Add E
window_hash += ord('E')
```

Then we take modulo `mod` to keep the value manageable.

So mentally:

```text
OLD WINDOW
   ↓
Remove left character
   ↓
Shift everything
   ↓
Add new right character
   ↓
NEW WINDOW
```

That's the rolling hash.

---

# 11. The complete Rabin–Karp flow

The algorithm can be visualized like this:

```text
              Pattern
                 │
                 ▼
          Calculate hash
                 │
                 ▼
          ┌─────────────┐
          │ Text Window │
          └──────┬──────┘
                 │
                 ▼
          Calculate hash
                 │
                 ▼
        Hashes equal?
          /          \
        NO            YES
         │             │
         ▼             ▼
    Slide window   Verify actual
                      strings
                         │
                    ┌────┴────┐
                    │         │
                   Same     Different
                    │         │
                    ▼         ▼
                  Match    Collision
```

Then we slide the window and repeat.

---

# 12. How to recognize Rabin–Karp in a problem

This is more useful than memorizing the implementation.

### Hint 1: Find a pattern inside a text

Classic string matching.

Think:

```text
KMP / Rabin-Karp
```

Then look at the constraints and what the problem actually needs.

---

### Hint 2: Compare many same-length substrings

This is a particularly strong Rabin–Karp signal.

For example:

> "Find whether any substring of length `k` is equal to another given string."

or:

> "Compare every window of length `k`."

Think:

```text
Rolling Hash
```

---

### Hint 3: Repeated substring comparisons

If you're repeatedly doing:

```text
text[i:i+k] == pattern
```

or comparing lots of substrings of the same length, hashing can often help.

---

### Hint 4: "Search efficiently in a large string"

If:

```text
n is huge
```

and checking every substring character-by-character would be expensive, Rabin–Karp is worth considering.

---

### Hint 5: Multiple pattern matching

Rabin–Karp becomes especially interesting when you're dealing with **multiple patterns of the same length**.

Instead of repeatedly comparing every pattern against every window, we can:

```text
Calculate hashes of all patterns
        ↓
Store them in a set
        ↓
Calculate rolling hash of each text window
        ↓
Check whether the hash exists
```

This is one of Rabin–Karp's useful extensions.

---

# 13. Rabin–Karp vs KMP

Both solve string matching, but their core ideas are different.

|                       | KMP                             | Rabin–Karp                           |
| --------------------- | ------------------------------- | ------------------------------------ |
| Main idea             | Reuse prefix/suffix information | Compare hashes                       |
| Key concept           | LPS                             | Rolling hash                         |
| Handles mismatch by   | Jumping in pattern              | Sliding window                       |
| Hashing               | No                              | Yes                                  |
| Collision possibility | No                              | Yes                                  |
| Typical use           | Single-pattern matching         | Pattern matching / multiple patterns |
| Extra space           | `O(m)`                          | Usually `O(1)` for one pattern       |

A good mental distinction is:

```text
KMP
↓
"Can I reuse part of what I already matched?"

Rabin-Karp
↓
"Can I quickly tell whether this window could be the pattern?"
```

---

# 14. Rabin–Karp vs Naive

|                       | Naive                       | Rabin–Karp             |
| --------------------- | --------------------------- | ---------------------- |
| Main idea             | Compare characters directly | Compare hashes first   |
| Worst-case            | `O(n × m)`                  | `O(n × m)`             |
| Typical/expected      | `O(n + m)`-ish for hashing  | `O(n + m)`             |
| Extra space           | `O(1)`                      | `O(1)` for one pattern |
| Main idea to remember | Try everything              | Rolling hash           |

One subtle point:

> **Rabin–Karp does not guarantee `O(n + m)` in the worst case.**

If many hash collisions occur, we may repeatedly perform actual string comparisons.

With a good hash function, however, the expected performance is very good.

---

# 15. The most important thing to understand about the code

There are really only three pieces.

### 1. Hash the pattern

```python
pattern_hash
```

This is our target fingerprint.

### 2. Hash the current text window

```python
window_hash
```

This is the fingerprint of the substring we're currently looking at.

### 3. Roll the window

```python
window_hash = (
    (window_hash - ord(text[i]) * high) * base
    + ord(text[i + m])
) % mod
```

This single operation:

```text
Remove → Shift → Add
```

moves us from one window to the next.

---

# 16. A small example

Suppose:

```text
Text:    ABCDEFG
Pattern: CDE
```

First window:

```text
ABC
```

Compare:

```text
hash(ABC) != hash(CDE)
```

No match.

Roll:

```text
ABC
 ↓
BCD
```

Again:

```text
hash(BCD) != hash(CDE)
```

Roll:

```text
BCD
 ↓
CDE
```

Now:

```text
hash(CDE) == hash(CDE)
```

So we verify:

```text
"CDE" == "CDE"
```

Yes!

Therefore:

```text
found = [2]
```

Then continue sliding if we want **all** occurrences.

---

# 17. Overlapping matches work naturally

Consider:

```text
Text:    AAAAA
Pattern: AAA
```

The windows are:

```text
AAA
AAA
AAA
```

So the answer is:

```text
[0, 1, 2]
```

Rabin–Karp doesn't need any special trick for this.

It simply keeps sliding the window one character at a time.

That's another nice property of the sliding-window approach.

---

# 18. Common mistakes

### Mistake 1 — Assuming equal hashes mean equal strings

Don't do:

```python
if pattern_hash == window_hash:
    found.append(i)
```

A collision is theoretically possible.

Instead:

```python
if pattern_hash == window_hash:
    if text[i:i + m] == pattern:
        found.append(i)
```

---

### Mistake 2 — Forgetting to remove the old leftmost character

When the window moves:

```text
ABCD → BCDE
```

you have to remove `A` from the old hash.

Otherwise the hash won't represent the new window.

---

### Mistake 3 — Forgetting the modulo

Hash values can become enormous.

Use:

```python
% mod
```

throughout the calculation.

---

### Mistake 4 — Forgetting the edge case

If:

```text
len(pattern) > len(text)
```

the pattern obviously cannot occur.

Return:

```python
[]
```

immediately.

---

# 19. Complexity

Let:

```text
n = length of text
m = length of pattern
```

### Hash preparation

```text
O(m)
```

### Sliding through the text

Expected:

```text
O(n)
```

because each window's hash is updated in constant time.

### Verification

Usually very small because hash matches are rare with a good hash.

Expected overall:

```text
O(n + m)
```

Worst case:

```text
O(n × m)
```

because of hash collisions.

### Space

For a single pattern:

```text
O(1)
```

apart from the returned list of matches.

---

# 20. The easiest way to remember Rabin–Karp

Think:

> **"Give every string a fingerprint."**

Then:

```text
Pattern
   ↓
Fingerprint

Text window
   ↓
Fingerprint

Compare
   ↓
Different → definitely not equal
Same      → verify
```

And to move to the next window:

```text
Remove
  ↓
Shift
  ↓
Add
```

That's Rabin–Karp.

---

# 21. Rabin–Karp Cheat Sheet

```text
RABIN-KARP
│
├── Purpose
│   └── Efficient pattern matching
│
├── Main idea
│   └── Compare hashes instead of strings first
│
├── Key concept
│   └── Rolling Hash
│
├── Window movement
│   ├── Remove left character
│   ├── Shift hash
│   └── Add new right character
│
├── Hashes different
│   └── Definitely not a match
│
├── Hashes same
│   └── Verify actual strings
│
├── Expected time
│   └── O(n + m)
│
├── Worst-case time
│   └── O(n × m)
│
├── Space
│   └── O(1) for a single pattern
│
└── Recognition hints
    ├── Find a pattern in text
    ├── Compare many same-sized substrings
    ├── Sliding window over strings
    ├── Repeated substring comparisons
    └── Multiple pattern matching
```

---

# 22. LeetCode Problems to Practice

Rabin–Karp isn't always explicitly required on LeetCode, so the best practice is to look for problems where **rolling hashes / substring hashing** are useful.

1. **[28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)**
   The classic pattern-matching problem. You can solve it with either KMP or Rabin–Karp.

2. **[1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)**
   One of the best problems for learning rolling hash. The usual approach combines **binary search + Rabin–Karp-style hashing**.

3. **[718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)**
   A useful problem for thinking about equal-length subarrays and hashing.

4. **[187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)**
   A very nice introduction to hashing fixed-length substrings. Since every DNA sequence has the same length, hashing fits naturally.

5. **[1062. Longest Repeating Substring](https://leetcode.com/problems/longest-repeating-substring/)**
   Another good rolling-hash problem, especially when combined with binary search.

---

# Final takeaway

Don't think of Rabin–Karp as:

> "I need to memorize this complicated hash formula."

Think of it as:

> **"I have a pattern and a bunch of same-sized windows. Give each one a fingerprint so I can compare them cheaply."**

Then remember the two core ideas:

```text
Hash comparison
      +
Rolling window
```

And whenever the hashes match:

```text
Same hash
   ↓
Verify actual substring
```

That's Rabin–Karp.
