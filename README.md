## What An Invariant Means

An **invariant** is a predicate (a logical property) $P(s)$ over your program state $s \in S$ that remains true at a chosen point in the algorithm. To prove correctness, an invariant must satisfy three conditions:

1. **Initialization:** $P(s_0)$ is true before the first iteration of the loop.
2. **Maintenance:** If $P(s)$ is true before an iteration, and the iteration transforms state $s \to s'$, then $P(s')$ is true before the next iteration.
3. **Termination:** When the loop terminates, the combination of $P(s_{\text{term}})$ and the termination condition implies the correctness of the final output.

Mental model:
```text
Invariant = the promise the algorithm keeps.
Update rule = how the algorithm restores the promise after new input threatens it.
Answer = what can be safely extracted while the promise is true.
```

### Direct Examples

#### 1. Binary Search (`[lo, hi)` Left-Closed, Right-Open)
* **Goal:** Find the first index $i$ in a sorted array where `nums[i] >= target`.
* **State:** Boundaries `lo` and `hi`.
* **Invariant:** *"The first index $i$ satisfying the condition (if it exists) lies in the interval `[lo, hi)`."*
* **Initialization:** `lo = 0`, `hi = len(nums)`. The target index must lie in `[0, len(nums))`.
* **Maintenance:** Let `mid = lo + (hi - lo) // 2`.
  * If `nums[mid] >= target`: $mid$ is a valid candidate, but there could be a smaller one to its left. The first index must lie in `[lo, mid]`. We update `hi = mid`.
  * If `nums[mid] < target`: No index $\le mid$ can satisfy the condition. The first index must lie in `[mid + 1, hi)`. We update `lo = mid + 1`.
* **Termination:** Ends when `lo == hi`. The interval `[lo, lo)` is empty. If an answer exists, it must be `lo`. Check `lo < len(nums) and nums[lo] >= target`.

#### 2. Sliding Window (`last_seen` Hash Map)
* **Goal:** Longest substring without duplicate characters.
* **State:** `start` (left pointer), `end` (right pointer), and `last_seen` map of `char -> index`.
* **Invariant:** *"At the beginning of iteration `end`, `start` is the smallest index such that `s[start:end]` has no duplicate characters, and `last_seen` maps every processed character to its most recent index."*
* **Maintenance:** We process `char = s[end]`.
  * If `char` was seen at `prev_idx = last_seen[char]` and `prev_idx >= start`, the active window contains a duplicate.
  * To restore the promise, we slide the left boundary past the duplicate: `start = prev_idx + 1`.
  * Update `max_len = max(max_len, end - start + 1)` and update the map: `last_seen[char] = end`.

| Pattern | State | Invariant |
|---|---|---|
| Hash map | Map | Before processing index `i`, the map summarizes exactly the processed prefix `nums[0:i]`. |
| Prefix sum | Map + Sum | Before index `i`, `count[s]` is the number of previous prefixes with sum `s`. |
| Sliding window | Left, Right | The current window is the longest valid window ending at `Right`, or the loop is actively shrinking until it is valid. |
| Binary search | Lo, Hi | The target index remains inside the search interval, or all values outside are impossible. |
| DFS/BFS | Visited Set | Once a node is marked visited/enqueued, it will not be processed again. |
| Monotonic stack | Stack | The stack stores unresolved candidates in monotonic order; when an item is popped, its answer is now known. |
| DP | DP Table | `dp[i]` is the exact optimal solution for the subproblem ending at `i` or using the first `i` items. |
| Bitwise | Mask / Accumulator | At step `k`, the accumulated value holds the invariant property for the first `k` bit positions or inputs. |

>[!warning]+ If the invariant is hard to state
>Do not assume the code will clarify it. Usually this means the pattern is misclassified, the state is missing, or the answer variable is being mixed with the recursive return value.

---

## Per-Problem Template

Use this before every solution:

```text
Problem:
Pattern:
State:
Invariant:
Update / transition:
Answer:
Complexity:
Edge cases:
```

Use this after every solution:

```text
Bug or hesitation:
Root cause:
What invariant would have prevented it:
Redo date:
```

Interview speaking script:

```text
Let me restate the problem.

The brute-force approach is ...
That costs ...

The pattern looks like ...
I will maintain ...
The invariant is ...

When I process ...
I update ...

Then I will test on ...
```

---

## Hint Protocol

Do not ask for a hint immediately. Spend five minutes in this order:

1. Write the brute force.
2. Identify the repeated work.
3. Ask whether a map, set, heap, stack, or prefix sum can remember it.
4. Check whether order matters: sorted array, monotonic relation, binary-searchable answer.
5. Check whether it is a contiguous subarray/window problem.
6. Check whether the input is secretly a graph/tree/grid.
7. If still stuck, state the brute force and ask a narrow pattern question.

Good hint request:

```text
I have the O(n^2) brute force. The repeated work seems to be recomputing information for overlapping subarrays. I am trying to decide whether prefix sums or a sliding window applies here. Could I get a small hint on the intended direction?
```

Bad hint request:

```text
I do not know what to do.
```

---

## Dated Schedule

### Thu May 28

Goal: setup and calibration.

- [x] Create this note.
- [ ] Choose interview language.
- [ ] Solve one easy and one medium without looking up the answer.
- [ ] Record the first real failure mode in [[Qualcomm Coding Interview Practice Plan#Attempt Log]].

### Fri May 29

Goal: remember the basic loop templates.

- [ ] Two Sum
- [x] Longest Substring Without Repeating Characters
- [ ] Binary Search
- [ ] Write the invariant for each from memory.

### Sat May 30 - Core Patterns

Block 1: Hash map / prefix sum.

- [ ] 1. Two Sum `[🔥 High ROI]`
- [ ] 49. Group Anagrams
- [ ] 128. Longest Consecutive Sequence
- [ ] 560. Subarray Sum Equals K `[🔥 High ROI]`

Block 2: Sliding window.

- [x] 3. Longest Substring Without Repeating Characters `[🔥 High ROI]`
- [ ] 567. Permutation in String
- [ ] 424. Longest Repeating Character Replacement
- [ ] 76. Minimum Window Substring `[🔥 High ROI]`

Block 3: Binary search.

- [ ] 704. Binary Search
- [ ] 33. Search in Rotated Sorted Array `[🔥 High ROI]`
- [ ] 153. Find Minimum in Rotated Sorted Array
- [ ] 875. Koko Eating Bananas `[🔥 High ROI]`
- [ ] 1011. Capacity To Ship Packages Within D Days

### Sun May 31 - Trees, Graphs, Stack, DP, Low-Level

Block 1: Trees & Graphs.

- [ ] 104. Maximum Depth of Binary Tree
- [ ] 112. Path Sum
- [ ] 543. Diameter of Binary Tree `[🔥 High ROI]`
- [ ] 236. Lowest Common Ancestor `[🔥 High ROI]`
- [ ] 200. Number of Islands `[🔥 High ROI]`
- [ ] 994. Rotting Oranges `[🔥 High ROI]`
- [ ] 207. Course Schedule `[🔥 High ROI]`

Block 2: Stack & DP.

- [ ] 20. Valid Parentheses
- [ ] 739. Daily Temperatures
- [ ] 84. Largest Rectangle in Histogram `[🔥 High ROI]`
- [ ] 70. Climbing Stairs
- [ ] 198. House Robber
- [ ] 322. Coin Change `[🔥 High ROI]`

Block 3: Qualcomm Low-Level & Bitwise (Crucial for HW/Silicon interviews).

- [ ] 136. Single Number `[🔥 High ROI]` (XOR Invariant)
- [ ] 191. Number of 1 Bits (Bit-Shifting/Masking)
- [ ] 190. Reverse Bits (Bitwise Reversal State)
- [ ] 268. Missing Number `[🔥 High ROI]` (XOR vs Sum arithmetic)
- [ ] 338. Counting Bits (DP on bit representation)

### Weekday Nights Until Interview

Each night is capped at two hours:

```text
20 min: review yesterday's mistakes
70 min: solve two problems
20 min: explain both out loud
10 min: write invariant, complexity, and one edge test
```

If the interview date arrives early in the June 1-5 window, stop learning new topics the night before. Redo failed problems only.

| Night | Focus | Problems |
|---|---|---|
| Night 1 | Hash / prefix | 1, 560, 128 |
| Night 2 | Sliding window | 3, 567, 76 |
| Night 3 | Binary search | 33, 875, 1011 |
| Night 4 | Trees & Low-Level | 543, 236, 136 |
| Night 5 | Graphs & Bits | 200, 994, 191 |
| Night 6 | Stack / DP | 739, 84, 322 |

Final night:

- [ ] Redo three failed problems.
- [ ] Recite the speaking script.
- [ ] Review only invariants and bugs.
- [ ] Sleep. No new topic.

---

## Pattern Sheets

### Hash Map / Set

Ask:

- What exactly is stored?
- Is it value -> index, value -> count, prefix_sum -> count, or canonical_key -> group?
- Why is lookup valid at this time?

Default invariant:

```text
Before processing nums[i], the table summarizes exactly the processed prefix nums[0:i].
```

Problems: 1, 49, 128, 560.

### Sliding Window

Ask:

- Is the window fixed size or variable size?
- What condition must the window satisfy?
- When the condition breaks, how do I restore it?

Default invariant:

```text
After the shrink loop, the window is the best valid candidate ending at right, or the smallest window that still satisfies the required coverage.
```

Problems: 3, 567, 424, 76.

### Binary Search

Ask:

- Am I searching an index or the answer value?
- Is the predicate monotonic?
- Does `mid` being feasible move `hi` or `lo`?

Default invariant for answer search:

```text
All values below lo are impossible. hi is feasible or remains inside the feasible region.
```

Problems: 704, 33, 153, 875, 1011.

### Trees

Ask:

- What does the recursive function return?
- Is the answer the return value, or a global/best value updated along the way?

Default invariant:

```text
The recursive function returns the correct value for the subtree rooted at node.
```

Problems: 104, 112, 543, 236, 102.

### Graphs / Grids

Ask:

- What is a node?
- What are edges/neighbors?
- When do I mark visited: enqueue time or pop time?

Default BFS invariant:

```text
The queue contains the current frontier; nodes already marked visited will not be enqueued again.
```

Problems: 200, 695, 994, 207.

### Monotonic Stack

Ask:

- What candidates are unresolved?
- Is the stack increasing or decreasing?
- What answer becomes known when I pop?

Default invariant:

```text
The stack stores unresolved indices in monotonic order.
```

Problems: 20, 739, 84.

### DP Basics

Ask:

- What does `dp[i]` mean in one sentence?
- Which earlier states are sufficient?
- What is the base case?

Default invariant:

```text
After filling dp[i], it is the optimal answer for the subproblem ending at i or using the first i items.
```

Problems: 70, 198, 322, 300.

### Bitwise & Low-Level

Ask:

- What physical state is represented by the bits (sign, representation, set bits)?
- How do logical operations (`&`, `|`, `^`, `~`) filter or combine information?
- What is the algebraic identity (e.g., `x ^ x = 0`, `x & (x - 1)` removes the lowest set bit)?

Default invariant:

```text
At step k, the accumulator contains the correct aggregated state (like parity or count) for all processed elements or the first k bits.
```

Problems: 136, 191, 190, 268, 338.

---

## High-Yield Hint Sheet

Use these only after the five-minute stuck protocol. Read the hint, then close the note and try again.

| Problem | First hint | Invariant to recover |
|---|---|---|
| 560. Subarray Sum Equals K | A subarray sum is the difference between two prefix sums. | Before index `i`, the map counts prefix sums seen before `i`. |
| 76. Minimum Window Substring | Expand until valid, then shrink while still valid. | When updating the answer, the window covers all required counts. |
| 33. Search in Rotated Sorted Array | At least one half around `mid` is sorted. | The target, if present, remains in `[lo, hi]`. |
| 875. Koko Eating Bananas | Search the eating speed, not the pile index. | Speeds below `lo` are impossible; feasible speeds stay on the right side. |
| 1011. Capacity To Ship Packages | Capacity is monotonic: larger capacity never needs more days. | `hi` is feasible; values below `lo` are impossible. |
| 543. Diameter of Binary Tree | Height is returned; diameter is updated separately. | `dfs(node)` returns subtree height, while `best` stores the largest path seen. |
| 236. Lowest Common Ancestor | If both sides return non-null, current node is the split point. | Return the node found in this subtree, if any. |
| 994. Rotting Oranges | Multi-source BFS starts from all initially rotten oranges. | The queue is the frontier of oranges rotting at the current minute. |
| 207. Course Schedule | Think indegree, not recursive guessing. | Indegree zero means no remaining prerequisites. |
| 84. Largest Rectangle in Histogram | When a bar is popped, its maximal rectangle height is known. | Stack indices have increasing heights. |
| 322. Coin Change | Build minimum coins for each amount. | After `dp[a]`, it is the minimum coins needed for amount `a`, or infinity if impossible. |

---

## Minimal Must-Do List

If time collapses, finish these first (focus heavily on the marked `[🔥 High ROI]` ones):

| Topic | Problems |
|---|---|
| Hash / prefix | 1 `[🔥 High ROI]`, 49, 128, 560 `[🔥 High ROI]` |
| Sliding window | 3 `[🔥 High ROI]`, 567, 424, 76 `[🔥 High ROI]` |
| Two pointers | 11 `[🔥 High ROI]`, 15, 42 `[🔥 High ROI]` |
| Binary search | 704, 33 `[🔥 High ROI]`, 153, 875 `[🔥 High ROI]`, 1011 |
| Stack | 20, 739, 84 `[🔥 High ROI]` |
| Trees | 104, 112, 236 `[🔥 High ROI]`, 543 `[🔥 High ROI]`, 102 |
| Graphs | 200 `[🔥 High ROI]`, 695, 994 `[🔥 High ROI]`, 207 `[🔥 High ROI]` |
| DP | 70, 198, 322 `[🔥 High ROI]` |
| Bitwise / Low-Level | 136 `[🔥 High ROI]`, 191, 190, 268 `[🔥 High ROI]`, 338 |

Do not spend the weekend on segment trees, advanced DP, or clever graph algorithms. A hard interview problem is often just two medium patterns glued together.

---

## Attempt Log

Fill this brutally. The point is to identify the bug pattern, not to feel productive.

| Date | Problem | Result | Failed because | Correct invariant | Redo |
|---|---|---|---|---|---|
| 2026-05-28 | 3, 136, 11, 268  |  |  |  |  |
| 2026-05-29 |  |  |  |  |  |
| 2026-05-30 |  |  |  |  |  |
| 2026-05-31 |  |  |  |  |  |
| 2026-06-01 |  |  |  |  |  |
| 2026-06-02 |  |  |  |  |  |
| 2026-06-03 |  |  |  |  |  |
| 2026-06-04 |  |  |  |  |  |

---

## Interview Checklist

Before coding:

- [ ] Restate the problem and constraints.
- [ ] Give brute force and cost.
- [ ] Name the pattern.
- [ ] Write state and invariant.
- [ ] Mention complexity target.

During coding:

- [ ] Keep variable names boring.
- [ ] Update answer only when invariant is true.
- [ ] For BFS, mark visited when enqueuing.
- [ ] For binary search, state what `lo`, `hi`, and `mid` mean.
- [ ] For recursion, separate return value from global answer.

Testing:

- [ ] Empty or minimum input.
- [ ] One element.
- [ ] Duplicates.
- [ ] Negative numbers, if relevant.
- [ ] Already sorted / reverse sorted.
- [ ] Boundary case: window length, index range, disconnected graph, impossible target.

>[!important]+ Target performance
>Easy: solve in 10 minutes.
>
>Medium: solve in 25-30 minutes.
>
>Hard: identify the pattern, communicate the invariant, and produce a partial correct solution if full solution does not fit.

---

## One-Sentence Reminders

- Hash map: "What have I seen before this index?"
- Prefix sum: "Which earlier prefix would make this subarray sum correct?"
- Sliding window: "Expand to include, shrink to restore."
- Binary search: "What half can I prove is impossible?"
- DFS/BFS: "What is a node, and when is it permanently visited?"
- Stack: "What unresolved candidate just got resolved?"
- DP: "What exactly does this cell mean?"

*Last updated: 2026-05-28*
