**Pattern**: Sliding Window

**State**:
- `start`: left boundary of the window.
- `end`: right boundary of the window (loop index).
- `freq`: frequency map of values (`0` and `1`) in the active window.
- `max_len`: tracks the maximum consecutive ones found.

**Invariant**:
- The active window `nums[start:end+1]` contains at most `k` zeros, so it can be converted to all ones by flipping them.

**Update Rule**:
- Add `nums[end]` to `freq`.
- While `freq.get(0, 0) > k`, we shrink the window from the left by decrementing the count of `nums[start]` and incrementing `start`.
- Update `max_len = max(max_len, end - start + 1)`.
