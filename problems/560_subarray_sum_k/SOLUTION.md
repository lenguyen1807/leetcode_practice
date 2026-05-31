**Pattern**: Prefix Sum + Hash Map

**State**:
- `curr_sum`: current running sum of the prefix `nums[0:i]`.
- `seen`: a hash map of `prefix_sum -> frequency` mapping prefix sums encountered so far.
- `count`: total count of subarrays summing to `k`.

**Invariant**:
- Before processing `nums[i]`, `seen` maps the exact frequencies of all prefix sums in `nums[0:i]`.
- A subarray summing to `k` ending at `i` is defined by `curr_sum - prefix_sum = k`, which rearranges to `prefix_sum = curr_sum - k`. The frequency of such valid prefixes is exactly `seen[curr_sum - k]`.

**Update Rule**:
- Add `nums[i]` to `curr_sum`.
- Add `seen.get(curr_sum - k, 0)` to `count`.
- Update `seen[curr_sum] = seen.get(curr_sum, 0) + 1`.
