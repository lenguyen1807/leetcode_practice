**Pattern**: Hash Map / Set

**State**:
- `nums_set`: a set containing all numbers in `nums` to achieve $\mathcal{O}(1)$ lookup.
- `max_len`: tracks the longest consecutive sequence found.

**Invariant**:
- We only start counting sequence lengths from elements `n` that are sequence boundaries (`n - 1 not in nums_set`). This ensures each element is processed at most twice, guaranteeing $\mathcal{O}(N)$ time complexity.

**Update Rule**:
- For each number `n` in `nums_set`:
  - If `n - 1 not in nums_set` (meaning `n` is the start of a consecutive sequence):
    - Increment `current_num` and `current_len` until `current_num + 1` is not in `nums_set`.
    - Update `max_len = max(max_len, current_len)`.
