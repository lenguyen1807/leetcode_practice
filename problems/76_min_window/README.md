**Pattern**: Sliding Window

**State**:
- `start`: left boundary of the window.
- `end`: right boundary of the window (loop index).
- `freq_t`: frequency map of required characters in `t`.
- `freq_s`: frequency map of characters in the current window `s[start:end+1]`.
- `have`: count of character requirements currently satisfied.
- `need`: count of distinct character requirements in `t`.
- `answer`: a list `[best_start, best_end]` representing the shortest valid substring.

**Invariant**:
- `freq_s` represents exactly the counts of characters in `s[start:end+1]`.
- When `have == need`, the current window covers all required counts, and we shrink the window from the left to search for the minimal valid window.

**Update Rule**:
- Add `s[end]` to `freq_s`. If `s[end]` is in `freq_t` and `freq_s[s[end]] == freq_t[s[end]]`, increment `have` by 1.
- While `have == need`, update `answer` if the current window is smaller, then decrement `freq_s[s[start]]`. If `s[start]` is in `freq_t` and `freq_s[s[start]] < freq_t[s[start]]`, decrement `have` by 1. Increment `start` by 1.
