**Pattern**: Two Pointer (Converging / Swapping)

**State**:
- `l`: left pointer of the segment being reversed.
- `r`: right pointer of the segment being reversed.

**Invariant**:
- For the `reverse(l, r)` helper function: At each step, all elements outside `[l, r]` (but within the target segment) have been successfully swapped, while the subsegment `arr[l:r+1]` remains to be reversed.

**Reversal Strategy (Three-Reversal Algorithm)**:
To rotate the array to the right by `k` steps in-place with $\mathcal{O}(1)$ extra memory:
1. First reverse the entire array: `reverse(0, n - 1)`.
2. Reverse the first `k` elements: `reverse(0, k - 1)`.
3. Reverse the remaining `n - k` elements: `reverse(k, n - 1)`.
