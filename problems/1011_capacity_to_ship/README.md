**Pattern**: Binary Search (on Answer Range) + Prefix Sum with Binary Search split detection

**State**:
- `lo`: minimum possible ship capacity (`max(weights)`). If we chose a smaller capacity, we couldn't ship the heaviest single package.
- `hi`: maximum possible ship capacity (`sum(weights)`).
- `answer`: minimum valid capacity found so far.

**Invariant**:
- All capacities strictly less than `lo` are impossible (they cannot ship the packages within `days` days).
- `hi` is feasible or remains inside the feasible region, and `answer` stores the best valid capacity found so far.

**Update / transition**:
- At each step, compute mid capacity `k = lo + (hi - lo) // 2`.
- Check if capacity `k` is feasible using a prefix sum array and binary search:
  - Keep `prefix_sum` array static.
  - To find how many packages we can ship on a given day starting from index `curr_idx` (with sum `prefix_sum[curr_idx]`):
    - Find the largest index `next_idx` such that `prefix_sum[next_idx] - prefix_sum[curr_idx] <= k`.
    - This is equivalent to finding the largest index `next_idx` where `prefix_sum[next_idx] <= prefix_sum[curr_idx] + k`.
    - Use binary search (`bisect_right`) to find this split point in $O(\log N)$ time.
  - Repeat this for at most `days` days. If we reach the end of the array, `k` is feasible: update `answer = mid` and search for smaller valid capacities (`hi = mid - 1`).
  - Otherwise, `k` is not feasible: search for larger capacities (`lo = mid + 1`).

**Complexity**:
- **Time Complexity**: $O(D \log N \log M)$ where $N$ is the number of packages, $D$ is the number of days, and $M = \text{sum(weights)} - \max(\text{weights})$.
  - Note: This is an $O(D \log N)$ feasibility check, which is an optimization over the standard $O(N)$ linear check when $D \log N < N$ (i.e. when the number of days $D$ is relatively small).
- **Space Complexity**: $O(N)$ to store the prefix sum array.

**Edge cases**:
- `days` is exactly 1 (requires `k = sum(weights)`).
- `days` is exactly the length of `weights` (requires `k = max(weights)`).

---

### Analysis of the Prefix Sum & Subtraction Idea

**The Subtraction Idea**:
You proposed using a prefix sum array and subtracting the cumulative weight of the shipped packages from the remaining suffix elements at each day step.
- *For example*: `[3, 5, 7, 11, 12, 16]` with `k = 6`
  - Day 1: Sum 5 is $\le 6$. Suffix becomes `[0, 0, 7 - 5, 11 - 5, 12 - 5, 16 - 5] = [0, 0, 2, 6, 7, 11]`.
  - Day 2: Sum 6 is $\le 6$. Suffix becomes `[0, 0, 0, 0, 7 - 11, 11 - 11]` ... and so on.

**Why this is a beautiful insight**:
- Mathematically, subtracting the sum $S$ of the prefix we just processed from the suffix elements and then checking if the new suffix value is $\le k$:
  $$\text{prefix\_sum}[j] - S \le k \iff \text{prefix\_sum}[j] \le S + k$$
- This equivalence means **we do not actually need to perform the expensive subtraction ($O(N)$ operation) at each step!**
- Instead, we can keep the `prefix_sum` array completely static, and simply search for the index where `prefix_sum[j] <= running_sum + k`.
- Since the prefix sum is monotonically increasing, we can use **binary search (`bisect_right`)** to find this index in $O(\log N)$ time rather than $O(N)$ time.

**Complexity comparison of Feasibility Check**:
1. **Subtraction Simulation**: $O(N \cdot D)$ time because modifying the array takes $O(N)$ per day.
2. **Standard Linear Scan**: $O(N)$ time by iterating through weights directly.
3. **Static Prefix Sum + Binary Search (Optimized)**: $O(D \log N)$ time.
   - For a small number of days $D$ (e.g. $D \ll N$), this is incredibly fast!
---

### Attempt Log - June 1, 2026

**Bug or hesitation**: 
1. Used Python array slicing (`pref[idx:]`) inside the binary search helper, which created relative indexes and triggered an infinite loop, as well as an $O(N)$ slicing overhead.
2. Naming mismatch between `mid` and `capacity` in the main binary search loop (`NameError`).

**Root cause**:
1. Misunderstanding of how `bisect_right` returns indexes when operating on a sliced array, and forgetting the copy-overhead of Python's slicing.
2. Typo in loop variables during binary search range updates.

**What invariant would have prevented it**:
- *Invariant*: `idx` must represent the absolute boundary in the original prefix sum array. Passing the `lo` parameter in `bisect_right(pref, target, lo=idx)` preserves this absolute indexing invariant and avoids copy overhead.

**Redo date**: June 1, 2026 (Solved)
