**Pattern**: Binary Search (Rotated Array)

**State**:
- `lo`: left boundary of the search interval.
- `hi`: right boundary of the search interval.
- `mid`: middle index of the current search interval.

**Invariant**:
- The target, if present in `nums`, must lie within the index interval `[lo, hi]`.

**Update Rule**:
- At least one half of the rotated array, divided by `mid`, is guaranteed to be sorted.
- If the left half is sorted (`nums[lo] <= nums[mid]`):
  - If `nums[lo] <= target < nums[mid]`, then the target must be in the left half: `hi = mid - 1`.
  - Otherwise, it must be in the right half: `lo = mid + 1`.
- Otherwise, the right half must be sorted (`nums[mid] <= nums[hi]`):
  - If `nums[mid] < target <= nums[hi]`, then the target must be in the right half: `lo = mid + 1`.
  - Otherwise, it must be in the left half: `hi = mid - 1`.
