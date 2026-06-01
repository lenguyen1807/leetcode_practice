**Pattern**: Sliding Window

**State**:
- `start`: left boundary of the window.
- `end`: right boundary of the window (loop index).
- `s1_budget`: frequency map of characters in `s1`.
- `s2_budget`: frequency map of characters in the active window `s2[start:end+1]`.

**Invariant**:
- The active window `s2[start:end+1]` is always a valid subsegment where no character exceeds its frequency count in `s1`.

**Update Rule**:
- Add `s2[end]` to `s2_budget`.
- If this causes `s2_budget[s2[end]] > s1_budget.get(s2[end], 0)`, we shrink the window from the left by incrementing `start` and decrementing counts in `s2_budget` until the budget is respected.
- After restoring validity, if `end - start + 1 == len(s1)`, we have found a permutation and return `True`.
