# KMP String Matching — Playbook

KMP (**Knuth–Morris–Pratt**) is one of those algorithms that looks unnecessarily complicated when you first see it.

You see things like:

```text
LPS
lps[i]
lps[j - 1]
length = lps[length - 1]
```

and immediately think:

> "Why are we doing all this? Can't I just compare the strings?" 😭

You absolutely can — and that's basically what the naive approach does.

The problem is that the naive approach keeps **rechecking characters that we've already learned something about**.

KMP's entire purpose is:

> **Don't redo work that you've already done.**

Once you understand that idea, the LPS array stops feeling like some magical formula and starts making sense.

---

## 1. What problem does KMP solve?

The classic problem is:

> **Find where a pattern occurs inside a text.**

For example:

```text
Text:    ABABDABABABABCABAB
Pattern: ABAB
```

The pattern appears at:

```text
0
5
7
15
```

So we want:

```text
[0, 5, 7, 15]
```

A straightforward solution would try the pattern at every possible position in the text.

That works.

But there is a problem...

---

# 2. The problem with the naive approach

Imagine:

```text
Text:    A A A A A A A A B
Pattern: A A A A B
```

We start matching:

```text
Text:    A A A A A A A A B
         ↑ ↑ ↑ ↑
Pattern: A A A A B
```

Four characters match.

Then:

```text
Text:    A A A A A A A A B
                 ↑
Pattern: A A A A B
                 ↑
```

Mismatch.

The naive approach basically says:

> "Cool. Let's start again from the next position."

And we compare all those `A`s again.

But think about it.

We **already know** that the text contained:

```text
AAAA
```

And our pattern also starts with:

```text
AAAA
```

There is no reason to throw that information away.

This is the observation KMP is built around.

---

# 3. The KMP idea in one sentence

If you remember only one thing from this entire playbook, remember this:

> **When a mismatch happens, KMP uses the part of the pattern that we already know can still match instead of starting over.**

That's it.

Everything else exists to make this idea possible.

---

# 4. The key question KMP asks

Suppose we've matched:

```text
A B A B A
```

and then we get a mismatch.

Instead of saying:

> "Start from zero."

KMP asks:

> **"Does the end of what I just matched look like the beginning of my pattern?"**

For:

```text
A B A B A
```

the answer is yes.

We have:

```text
A B A
```

at both ends:

```text
A B A B A
↑ ↑ ↑
A B A

    ↑ ↑ ↑
    A B A
```

So we already have a valid partial match of length `3`.

Why compare those characters again?

We don't.

We reuse them.

---

# 5. Prefix and suffix

This is where the term **LPS** comes from.

### Prefix

A prefix starts from the beginning.

For:

```text
ABABA
```

the prefixes are:

```text
A
AB
ABA
ABAB
ABABA
```

### Suffix

A suffix ends at the end.

```text
A
BA
ABA
BABA
ABABA
```

The common ones are:

```text
A
ABA
ABABA
```

But there's an important detail.

We don't count the entire string itself.

So the longest **proper** prefix which is also a suffix is:

```text
ABA
```

Length:

```text
3
```

Hence:

```text
LPS = 3
```

---

# 6. What exactly is LPS?

LPS stands for:

> **Longest Proper Prefix which is also a Suffix**

For every position in the pattern, we calculate this value.

Take:

```text
Pattern = ABABAC
```

The LPS array is:

```text
[0, 0, 1, 2, 3, 0]
```

Let's understand it rather than memorizing it.

| Substring | Longest prefix = suffix | LPS |
| --------- | ----------------------- | --: |
| `A`       | —                       |   0 |
| `AB`      | —                       |   0 |
| `ABA`     | `A`                     |   1 |
| `ABAB`    | `AB`                    |   2 |
| `ABABA`   | `ABA`                   |   3 |
| `ABABAC`  | —                       |   0 |

So:

```text
Pattern: A B A B A C
Index:   0 1 2 3 4 5
LPS:     0 0 1 2 3 0
```

---

# 7. What does `lps[i]` actually mean?

This is extremely important.


> **"`lps[i]` => how much of the beginning of the pattern I can reuse after reaching position `i`."**

More precisely:

```text
lps[i] = length of the longest proper prefix of pattern[0:i+1] that is also a suffix
```

For example:

```text
Pattern = A B A B A
Index   = 0 1 2 3 4
LPS     = 0 0 1 2 3
```

At index `4`:

```text
ABABA
```

ends with:

```text
ABA
```

and starts with:

```text
ABA
```

Therefore:

```text
lps[4] = 3
```

---

# 8. Why is LPS useful?

Suppose:

```text
Pattern = ABABAC
```

and we've matched:

```text
ABABA
```

Then the next character doesn't match.

We could restart:

```text
ABABAC
^
```

But LPS tells us:

```text
lps[4] = 3
```

which means:

```text
ABA
```

is still valid.

So instead of:

```text
ABABA
     ↓
     mismatch
     ↓
     restart from 0
```

we do:

```text
ABABA
  ↓
  reuse ABA
```

That's the entire reason we built LPS in the first place.

---

# 9. The most important KMP line

You'll eventually see this:

```python
j = lps[j - 1]
```

At first, it looks completely random.

It's not.

Suppose:

```text
j = 5
```

That means we've matched five characters of the pattern.

Now we get a mismatch.

Instead of doing:

```python
j = 0
```

we ask:

> "Among those five matched characters, how much of the pattern can I still reuse?"

The answer is stored at:

```python
lps[4]
```

because:

```python
j - 1
```

is the index of the last successfully matched character.

So:

```python
j = lps[j - 1]
```

means:

> **"Fall back to the next largest prefix that we already know matches."**

This is the line that makes KMP KMP.

---

# 10. Why don't we move `i` backwards?

This is another beautiful part of KMP.

During searching:

```python
i = text pointer
j = pattern pointer
```

When we get a mismatch:

```python
text[i] != pattern[j]
```

we do:

```python
j = lps[j - 1]
```

We **don't change `i`**.

Why?

Because the current text character hasn't been successfully matched against the new pattern position yet.

We're simply saying:

> "Maybe this same text character can match an earlier position in the pattern."

So:

```text
Text pointer → keeps moving forward
Pattern pointer → can jump backward
```

This is one of the reasons KMP stays linear.

---

# 11. Building the LPS array

There are two pointers:

```python
i
length
```

Think of them as:

* `i` → the position we're currently trying to calculate
* `length` → how much prefix/suffix we currently have

Initially:

```python
i = 1
length = 0
```

Why `i = 1`?

Because:

```python
lps[0] = 0
```

A single character cannot have a proper prefix.

---

## Case 1 — Characters match

If:

```python
pattern[i] == pattern[length]
```

we found another matching character.

So:

```python
length += 1
lps[i] = length
i += 1
```

Simple.

---

## Case 2 — Characters don't match, but `length > 0`

This is the interesting case.

We have some prefix/suffix match, but extending it failed.

Don't throw everything away.

Instead:

```python
length = lps[length - 1]
```

We're asking:

> "Okay, this prefix was too long. What's the next smaller prefix that might still work?"

---

## Case 3 — Characters don't match and `length == 0`

There's nothing left to fall back to.

So:

```python
lps[i] = 0
i += 1
```

That's it.

---

# 12. Searching using LPS

Once the LPS array is ready, searching becomes fairly straightforward.

We have:

```python
i = 0
j = 0
```

where:

```text
i → text
j → pattern
```

### If characters match:

```python
i += 1
j += 1
```

### If the entire pattern matches:

```python
found.append(i - j)
```

Then:

```python
j = lps[j - 1]
```

This is important because it allows us to find **overlapping matches**.

### If there's a mismatch and `j > 0`:

```python
j = lps[j - 1]
```

### If there's a mismatch and `j == 0`:

```python
i += 1
```

---

# 13. The complete mental model

You can reduce the entire algorithm to this:

```text
             PATTERN
                │
                ▼
          Build LPS array
                │
                ▼
      Start scanning the text
                │
                ▼
        Characters match?
          /          \
        YES           NO
         │             │
         ▼             ▼
   Move both       j > 0?
     forward       /    \
                  YES     NO
                   │       │
                   ▼       ▼
               Use LPS   Move text
                   │      forward
                   │
                   └───────┐
                           │
                           ▼
                       Continue
```

The important part is:

```text
Mismatch
   ↓
Have we matched something already?
   ↓
YES
   ↓
Use LPS
   ↓
Don't restart
```

---

# 14. How to recognize KMP in a DSA problem

This is probably more useful than memorizing the implementation.

When you see a problem, look for these hints.

### Hint 1: "Find a pattern in a string"

Classic KMP territory.

For example:

> Find all occurrences of `pattern` in `text`.

Immediately think:

```text
KMP
```

---

### Hint 2: "Find the first occurrence"

For example:

> Given `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`.

This is essentially the classic string matching problem.

Think:

```text
KMP
```

---

### Hint 3: "Find all occurrences"

If the problem asks for:

```text
all starting indices
```

KMP is a very natural solution.

---

### Hint 4: "Repeated pattern / prefix / suffix"

If the problem starts talking about:

```text
prefix
suffix
border
repeated prefix
repeated substring
```

your KMP radar should go off.

Especially if the problem involves the **LPS / prefix-function** concept.

---

### Hint 5: "String matching with huge inputs"

If:

```text
text = huge
pattern = huge
```

and a naive `O(n × m)` solution might be too slow, KMP is a candidate.

---

### Hint 6: "Don't recheck characters"

Sometimes the problem statement won't mention KMP at all.

Instead, you'll notice something like:

> We need to efficiently find whether a pattern occurs inside another string.

Ask yourself:

> "If I mismatch after matching a large part, can I reuse some of what I already matched?"

If yes, KMP might be useful.

---

# 15. A quick KMP decision checklist

When solving a string problem, ask:

```text
┌─────────────────────────────────────┐
│ Is there a text + pattern?          │
└──────────────────┬──────────────────┘
                   │
                  YES
                   │
                   ▼
┌─────────────────────────────────────┐
│ Do I need to find pattern matches?  │
└──────────────────┬──────────────────┘
                   │
                  YES
                   │
                   ▼
┌─────────────────────────────────────┐
│ Can matches overlap / repeat?       │
└──────────────────┬──────────────────┘
                   │
                  YES
                   │
                   ▼
              Think KMP
```

It's not a guarantee that KMP is the best solution, but it's a very strong signal.

---

# 16. KMP vs Naive String Matching

|                       | Naive              | KMP                    |
| --------------------- | ------------------ | ---------------------- |
| Main idea             | Try every position | Reuse previous matches |
| Worst case            | `O(n × m)`         | `O(n + m)`             |
| Extra space           | `O(1)`             | `O(m)`                 |
| Uses LPS              | No                 | Yes                    |
| Good for huge strings | Sometimes          | Yes                    |
| Main difficulty       | Very easy          | Understanding LPS      |

Where:

```text
n = text length
m = pattern length
```

---

# 17. KMP vs Rabin-Karp

You'll sometimes see both algorithms used for pattern matching.

### KMP

Uses:

```text
prefix/suffix structure
```

### Rabin-Karp

Uses:

```text
rolling hash
```

Very roughly:

```text
Exact structural matching → KMP
Hash-based matching      → Rabin-Karp
```

KMP is deterministic, while Rabin-Karp typically relies on hashing and has collision considerations.

For most standard single-pattern matching questions, KMP is a very solid choice.

---

# 18. Don't confuse LPS with "longest prefix"

This is a common mistake.

For:

```text
ABABA
```

the answer isn't:

```text
ABABA
```

because the **whole string isn't a proper prefix**.

It is:

```text
ABA
```

So:

```text
LPS = 3
```

Always remember:

> **Proper = cannot be the entire string.**

---

# 19. Don't make this common mistake

When there is a mismatch:

```python
elif j != 0:
    j = lps[j - 1]
```

Don't do:

```python
j = 0
```

That destroys the whole advantage of KMP.

You're essentially turning your KMP into a much less clever algorithm.

The whole point is:

```text
Mismatch
   ↓
Reuse previous information
   ↓
LPS
```

---

# 20. Overlapping matches

KMP is particularly nice when matches overlap.

Consider:

```text
Text:    AAAAA
Pattern: AAA
```

The occurrences start at:

```text
0
1
2
```

After finding the first:

```text
AAA
```

we don't completely restart.

The pattern itself has useful prefix/suffix information:

```text
AAA
```

has:

```text
AA
```

as both prefix and suffix.

So:

```python
j = lps[j - 1]
```

lets us continue looking for the overlapping occurrence.

This is one of the places where KMP really shines.

---

# 21. Complexity

Let:

```text
n = length of text
m = length of pattern
```

### Building LPS

```text
O(m)
```

### Searching

```text
O(n)
```

### Total

```text
O(n + m)
```

### Space

```text
O(m)
```

The key reason searching stays linear is that although `j` can move backward, the text pointer `i` never moves backward.

---

# 22. The code skeleton to remember

You don't need to memorize every comment.

The core LPS logic is:

```python
i, length = 1, 0

while i < m:
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1

    elif length != 0:
        length = lps[length - 1]

    else:
        i += 1
```

And the core search logic is:

```python
i, j = 0, 0

while i < n:
    if text[i] == pattern[j]:
        i += 1
        j += 1

        if j == m:
            # Found a match
            j = lps[j - 1]

    elif j != 0:
        j = lps[j - 1]

    else:
        i += 1
```

The two lines worth remembering most are:

```python
length = lps[length - 1]
```

and:

```python
j = lps[j - 1]
```

Both have the same fundamental meaning:

> **"I can't continue with the current match. What's the next smaller prefix that I can safely reuse?"**

---

# 23. KMP in one example

Let's say:

```text
Pattern = ABABAC
```

Its LPS:

```text
Index:   0 1 2 3 4 5
Pattern: A B A B A C
LPS:     0 0 1 2 3 0
```

Suppose we matched:

```text
ABABA
```

and then:

```text
C ≠ B
```

Instead of:

```text
j = 0
```

we look at:

```text
lps[4] = 3
```

So:

```text
j = 3
```

We reuse:

```text
ABA
```

Then continue.

That's KMP.

---

# 24. The easiest way to remember KMP

Think of KMP as having **two jobs**.

### Job 1 — Learn the pattern

```text
Pattern
   ↓
Find repeated prefix/suffix structure
   ↓
LPS
```

### Job 2 — Use what you learned

```text
Text + Pattern
      ↓
Mismatch
      ↓
Look at LPS
      ↓
Skip unnecessary comparisons
```

So:

> **LPS is basically the pattern's memory.**

The pattern remembers:

> "If I fail here, I don't necessarily have to start from zero."

That's probably the most useful mental model for remembering KMP.

---

# 25. When KMP is probably overkill

Not every string problem needs KMP.

If:

```text
n, m <= 100
```

and a simple solution is perfectly fast, don't force KMP just because you know it.

Also, if the problem is primarily about:

* anagrams
* character frequencies
* palindromes
* subsequences
* edit distance
* dynamic programming over strings

KMP may not be relevant.

KMP is specifically about exploiting **pattern structure during string matching**.

---

# 26. KMP Cheat Sheet

```text
KMP
│
├── Purpose
│   └── Efficient pattern matching
│
├── Main idea
│   └── Don't redo comparisons we've already done
│
├── Key concept
│   └── LPS
│
├── LPS
│   └── Longest Proper Prefix which is also a Suffix
│
├── On mismatch while building LPS
│   └── length = lps[length - 1]
│
├── On mismatch while searching
│   └── j = lps[j - 1]
│
├── Text pointer
│   └── Never moves backward
│
├── Time
│   └── O(n + m)
│
├── Space
│   └── O(m)
│
└── Recognition hints
    ├── Find pattern in text
    ├── Find all occurrences
    ├── Find first occurrence
    ├── Repeated prefix/suffix
    ├── Overlapping matches
    └── Huge strings where O(n × m) is too slow
```

---

# 27. LeetCode Problems to Practice

Here are some good problems where KMP or the **prefix-function/LPS idea** is directly useful:

1. **[28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)**
   This is the classic KMP problem. If you want to make sure you actually understand KMP, start here.

2. **[459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)**
   One of the best problems for understanding how the LPS array reveals repeating structure in a string.

3. **[214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)**
   A more interesting application of KMP. The trick is to build an LPS/prefix-function over a cleverly constructed string.

4. **[686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/)**
   Great practice for combining string construction with efficient pattern matching.

5. **[1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)**
   This one is especially good for understanding what the LPS array *really represents*, because the answer is essentially the final LPS value.

6. **[3008. Find Beautiful Indices in the Given Array II](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/)**
   A harder application where efficient occurrence finding becomes important.