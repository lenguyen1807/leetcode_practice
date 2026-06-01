**Pattern**: Two Pointer

**State**:
- `left`
- `right`
- `max_area`

**Initlization**:
- `left = 0` and `right = N - 1` because we assume `max_area` is the area between the whole array.

**Invariant**: 
- `right > left`.
- Between `left` and `high`, there is an optimal area.

**Update Rule**: How we can shrink the `arr[left:right]` such that the invariant is preserve?
- Let's see, if `arr[left] < arr[right]` then our container area is limited by `left`. We will find a better `arr[i]` where `left < i < right`, we will have two cases:
    - `arr[i] > arr[left]` then our area is still limited by `left` and `i - left < right - left` therefore `area(arr[left:i]) < area(arr[left:right])`
    - `arr[i] < arr[left]` is even worse, we are now limited by `i`, we have width and height all smaller so the area should be smaller
    - So for any `i` we choose, it's always worse than current area, so we can safely discard current `left` and shrink the space `left = left + 1`.
- The other case, `arr[right] <= arr[left]` is the same. So we can safely disacrd with `right = right - 1`.
- After all iteration, we will record all largest area in `max_area = max(max_area, min(arr[left], arr[right]) * (right - left))`.

**Better note**:
We do not move the shorter pointer because the taller pointer is “better.”
We move the shorter pointer because the shorter pointer has been fully exhausted.