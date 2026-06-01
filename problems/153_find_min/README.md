**Pattern**: Binary Search (Rotated Array Pivot)

**State**:
- `lo`: left boundary of the search space.
- `hi`: right boundary of the search space.
- `mid`: middle index of the current search space.

**Invariant**:
- The minimum element of `nums` is always contained within the index interval `[lo, hi]`.

**Update Rule**:
- We compare the middle element `nums[mid]` with the rightmost element `nums[hi]`:
  - If `nums[mid] > nums[hi]`, `mid` belongs to the larger left-rotated segment, which means the drop (pivot) and the absolute minimum must lie strictly to the right of `mid`: `lo = mid + 1`.
  - Otherwise (`nums[mid] <= nums[hi]`), the right half `nums[mid:hi+1]` is normally sorted. The absolute minimum could be `nums[mid]` itself, or it could lie strictly to the left of `mid`: `hi = mid`.
- The loop terminates when `lo == hi`, leaving both pointing exactly to the minimum element.
