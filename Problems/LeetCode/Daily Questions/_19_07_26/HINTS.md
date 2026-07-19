# Intuition

We need to build the **smallest lexicographical subsequence** that contains every distinct character **exactly once**.

There are two things we need to take care of:

1. Every distinct character should appear only once.
2. Among all such valid subsequences, we want the lexicographically smallest one.

The first condition is easy—we can simply keep a set of characters that are already included.

The second condition is where the challenge lies.

Suppose we've already built a partial answer and now encounter a smaller character.

For example,

```
Current answer: "bc"
Next character: "a"
```

It would clearly be better if `"a"` came before `"b"` and `"c"`.

But can we simply remove `"b"` and `"c"`?

Only if they appear again later in the string. Otherwise, we'd lose them forever, making the answer invalid.

So before removing any character, we must ensure that we'll get another chance to include it later.

This naturally leads to the idea of always keeping the answer as "small" as possible while never throwing away the last occurrence of any character.

---

# Key Observation

Before processing the string, record the **last occurrence** of every character.

Now, while building the answer:

- Skip characters that are already included.
- Otherwise, compare the current character with the last character in our answer.

If

- the current character is smaller,
- and the last character will appear again later,

then keeping the larger character now is never optimal.

We can safely remove it and add it back later.

This process can repeat multiple times until the answer is as small as possible.

---

# Why a Monotonic Stack?

Notice what we're doing.

Whenever we find a smaller character, we keep removing larger characters from the end of our current answer (as long as they appear again later).

This "keep popping from the end while a condition holds" is exactly the behavior of a **monotonic stack**.

The stack represents our current subsequence.

Whenever a better character arrives, we remove larger characters that can safely be placed later.

---

# Algorithm

1. Store the last index of every character.
2. Maintain:
   - a stack representing the current answer,
   - a set of characters already included.
3. Iterate through the string.
4. If the character is already present in the answer, skip it.
5. Otherwise:
   - While
     - the stack isn't empty,
     - the current character is smaller than the stack's top,
     - and the top character appears again later,
     
     pop it from the stack and remove it from the set.
6. Push the current character onto the stack and mark it as included.
7. Join the stack into the final answer.

---

# Dry Run

### Input

```
s = "cbacdcbc"
```

Last occurrences:

```
c -> 7
b -> 6
a -> 2
d -> 4
```

| Character | Stack | Action |
|-----------|-------|--------|
| c | c | Add c |
| b | b | Pop c (appears later), add b |
| a | a | Pop b (appears later), add a |
| c | ac | Add c |
| d | acd | Add d |
| c | acd | Already included |
| b | acdb | Can't pop d (no later d), so add b |
| c | acdb | Already included |

Final answer:

```
acdb
```

---

# Correctness

Whenever we remove a character from the stack, we know it appears again later. Therefore, removing it never prevents us from including every distinct character exactly once.

We only remove a character when a smaller one can take its place, making the resulting subsequence lexicographically smaller.

If a character does **not** appear later, we never remove it, since that would make it impossible to include all distinct characters.

Thus, every decision is both **safe** and **locally optimal**, producing the lexicographically smallest valid subsequence.

---

# Complexity Analysis

- Building the last occurrence map takes **O(n)**.
- Every character is pushed onto the stack at most once.
- Every character is popped from the stack at most once.

Therefore,

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(26)` for lowercase English letters (or `O(k)` where `k` is the number of distinct characters).

---

# Code

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store the last occurrence of every character
        lastPos = {}
        for i, char in enumerate(s):
            lastPos[char] = i

        stack = []
        included = set()

        for i, char in enumerate(s):
            # Skip duplicate characters
            if char in included:
                continue

            # Remove larger characters if they appear again later
            while (
                stack
                and char < stack[-1]
                and lastPos[stack[-1]] > i
            ):
                included.remove(stack.pop())

            stack.append(char)
            included.add(char)

        return "".join(stack)
```