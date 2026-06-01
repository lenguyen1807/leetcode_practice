**Pattern**: Sliding Window

**State**:
- `end`: the right pointer (current index of the loop).
- `start`: the left pointer of sliding window.
- `last_seen`: a hash map that mapppings each character to *its most recent* index in the string.
- `max_len`: maximum string length.

**Invariant**: At the beginning of each iteration:
- `start`: is the *smallest index* such that `s[start:end]` is a substring without duplicated.
- `last_seen`: maps every character processed so far (`s[0:end-1]`) to its most recent index.

**Update Rule**:
- If current character (`s[end]`) has been seen (`s[end] in last_seen`) and that seen is in our substring range (`last_seen[s[end]] >= start`) then there is duplicate.
- If duplicate, we move `start` to after that seen character (`start = last_seen[s[end]] + 1`) so that `s[start:end]` is a valid substring such that it has no duplicated and `start` is the smallest index.
- Or else, we keep maintaining our `last_seen` by setting `last_seen[char] = end` (current index).
- We also need to maintain `max_len` by updating it using `max(max_len, end - start + 1)`.