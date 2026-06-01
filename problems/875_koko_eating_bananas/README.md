**Pattern**: Binary Search (on Answer Range)

**State**:
- `lo`: minimum possible eating speed (1)
- `hi`: maximum possible eating speed (`max(piles)`)
- `answer`: minimum valid eating speed found so far

**Invariant**:
- All speeds strictly less than `lo` are impossible (they require more than `h` hours).
- `hi` is feasible or remains inside the feasible region, and `answer` stores the best valid speed found so far.

**Update / transition**:
- At each step, compute mid speed `k = lo + (hi - lo) // 2`.
- Calculate the total time: `t = sum(math.ceil(p / k) for p in piles)`.
- If `t <= h`, this speed is feasible. Record it: `answer = min(answer, k)` and search for smaller valid speeds: `hi = k - 1`.
- If `t > h`, this speed is too slow. Search for larger speeds: `lo = k + 1`.

**Complexity**:
- **Time Complexity**: $O(N \log M)$ where $N$ is the number of piles and $M = \max(\text{piles})$.
- **Space Complexity**: $O(1)$ auxiliary space.

**Edge cases**:
- `h` is exactly equal to the number of piles (requires `k = max(piles)`).
- Very large pile sizes (up to $10^9$).

---

### Previous Code Analysis & Retrospective

**Bug or hesitation**:
1. **Materializing Search Space**: Attempted `es = list(range(1, sorted_piles[-1] + 1))`. With $10^9$ constraints, this triggers a Memory Limit Exceeded (MLE) error due to massive memory allocation.
2. **Simulating Time vs. Calculating Time**: Attempted to simulate the eating process hour-by-hour with nested loops. This triggers a Time Limit Exceeded (TLE) error.
3. **Binary Search Strict Equality**: Returned immediately when `t == h` with `return mid`, which can miss the absolute *minimum* speed if multiple speeds produce `h` hours.
4. **Unnecessary Sorting**: Unnecessarily sorted the piles first ($O(N \log N)$), which is redundant since the order of piles does not affect Koko's total eating time.

**Root cause**:
- Simulating the step-by-step physical process instead of analyzing the underlying mathematical properties (independent piles, $\lceil p / k \rceil$ per pile) and recognizing the monotonic property of the speed-to-time relation.

**What invariant would have prevented it**:
- *All speeds strictly less than `lo` are impossible.*
- *Continuous bounds over a virtual search space rather than physical array initialization.*
