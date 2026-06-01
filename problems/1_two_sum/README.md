**Pattern**: Hash Map

**State**:
- `seen`: a hash map of `value -> index` mapping previously seen elements in the prefix.

**Invariant**:
- Before processing index `i`, `seen` contains all elements in the prefix `nums[0:i]` mapped to their respective indices.

**Update Rule**:
- Check if `target - nums[i]` exists in `seen`. If it does, a valid pair has been found: return `[seen[target - nums[i]], i]`.
- Otherwise, record `nums[i]` in `seen`: `seen[nums[i]] = i`.
