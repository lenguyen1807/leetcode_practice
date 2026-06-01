**Pattern**: Sliding Window

**State**:
- `start`: left boundary of the window.
- `end`: right boundary of the window (loop index).
- `freq`: frequency map of characters in the active window `s[start:end+1]`.
- `max_len`: tracks the longest valid substring found.

**Invariant**:
- The active window `s[start:end+1]` can be converted into a string of repeating characters using at most `k` replacements. 
- That is, the replacement cost `(end - start + 1) - max_freq <= k`, where `max_freq` is the frequency of the most frequent character in the current window.

**Update Rule**:
- Add `s[end]` to `freq`.
- Find the most frequent character in the window `max_c = max(freq, key=freq.get)`.
- While `(end - start + 1) - freq[max_c] > k`, we shrink the window from the left by decrementing the count of `s[start]`, incrementing `start`, and recomputing `max_c`.
- Update `max_len = max(max_len, end - start + 1)`.
