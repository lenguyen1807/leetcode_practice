# Qualcomm Interview Practice Plan

Focus order:

1. **Strengths:** Sliding Window, Two Pointers, Binary Search — include harder problems.
2. **Secondary practice:** BFS / DFS / Heap — medium problems only.
3. **Qualcomm low-level:** Bitwise, arrays, integer reasoning.
4. **Skip for now:** DP, hard graph algorithms, segment trees, advanced tricks.

---

## Core Invariant Reminder

An **invariant** is the promise your algorithm keeps true while it runs.

```text
Invariant = the promise the algorithm keeps.
Update rule = how the algorithm restores the promise.
Answer = what can be safely extracted while the promise is true.
```

Before coding, say:

```text
Pattern:
State:
Invariant:
Update / transition:
Answer:
Complexity:
Edge cases:
```

After solving, record:

```text
Bug or hesitation:
Root cause:
Invariant that would have prevented it:
Redo needed? yes/no
```

---

## Interview Speaking Script

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

Do not ask for a hint immediately. Spend five minutes:

1. Write the brute force.
2. Identify repeated work.
3. Ask if a map, set, heap, stack, prefix sum, or sorted order helps.
4. Check whether it is contiguous: subarray / substring / window.
5. Check whether a monotonic predicate allows binary search.
6. Check whether the input is secretly a graph/tree/grid.

Good hint request:

```text
I have the O(n^2) brute force. The repeated work seems to be recomputing information for overlapping subarrays. I am deciding between prefix sums and sliding window. Could I get a small direction hint?
```

---

# Problem Sets

Legend:

- `[x]` solved in `problems/`
- `[ ]` not solved yet
- `🔥` high ROI for tomorrow
- `Hard` only for your strength areas

---

## Set 1 — Sliding Window / Substring / Subarray

Default invariant:

```text
After the shrink loop, the window is valid, or it is the smallest window that still satisfies the required coverage.
```

Ask:

- Fixed size or variable size?
- What exact condition makes the window valid?
- When invalid, what must move: left pointer, counts, or both?

### Must-do

- [x] 3. Longest Substring Without Repeating Characters `🔥`
- [x] 567. Permutation in String `🔥`
- [x] 424. Longest Repeating Character Replacement `🔥`
- [x] 76. Minimum Window Substring `🔥 Hard`
- [x] 1004. Max Consecutive Ones III
- [ ] 209. Minimum Size Subarray Sum `🔥`
- [ ] 438. Find All Anagrams in a String
- [ ] 713. Subarray Product Less Than K
- [ ] 904. Fruit Into Baskets
- [ ] 930. Binary Subarrays With Sum
- [ ] 1248. Count Number of Nice Subarrays
- [ ] 1658. Minimum Operations to Reduce X to Zero

### Hard strength practice

- [x] 30. Substring with Concatenation of All Words `Hard`
- [ ] 239. Sliding Window Maximum `Hard / Heap or Deque`
- [ ] 480. Sliding Window Median `Hard / Heap`
- [ ] 992. Subarrays with K Different Integers `Hard`

---

## Set 2 — Two Pointers

Default invariant:

```text
Everything outside the active pointer range has already been proven impossible or already processed correctly.
```

Ask:

- Is the array sorted?
- Do both pointers move inward, or does one chase the other?
- What case lets me discard a side safely?

### Must-do

- [x] 11. Container With Most Water `🔥`
- [x] 189. Rotate Array
- [ ] 15. 3Sum `🔥`
- [ ] 167. Two Sum II - Input Array Is Sorted
- [ ] 283. Move Zeroes
- [ ] 344. Reverse String
- [ ] 345. Reverse Vowels of a String
- [ ] 392. Is Subsequence
- [ ] 611. Valid Triangle Number
- [ ] 845. Longest Mountain in Array
- [ ] 977. Squares of a Sorted Array

### Hard strength practice

- [ ] 42. Trapping Rain Water `🔥 Hard`
- [ ] 16. 3Sum Closest
- [ ] 18. 4Sum
- [ ] 31. Next Permutation

---

## Set 3 — Binary Search

Default invariant for answer search:

```text
All values below lo are impossible. hi is feasible or remains inside the feasible region.
```

Ask:

- Am I searching an index or the answer value?
- Is the predicate monotonic?
- If `mid` is feasible, do I move `hi` or `lo`?

### Must-do

- [ ] 704. Binary Search
- [x] 33. Search in Rotated Sorted Array `🔥`
- [x] 153. Find Minimum in Rotated Sorted Array `🔥`
- [x] 875. Koko Eating Bananas `🔥`
- [x] 1011. Capacity To Ship Packages Within D Days `🔥`
- [ ] 34. Find First and Last Position of Element in Sorted Array
- [ ] 35. Search Insert Position
- [ ] 74. Search a 2D Matrix
- [ ] 162. Find Peak Element
- [ ] 278. First Bad Version
- [ ] 540. Single Element in a Sorted Array
- [ ] 658. Find K Closest Elements
- [ ] 852. Peak Index in a Mountain Array
- [ ] 981. Time Based Key-Value Store

### Hard strength practice

- [ ] 4. Median of Two Sorted Arrays `Hard`
- [ ] 410. Split Array Largest Sum `Hard`
- [ ] 668. Kth Smallest Number in Multiplication Table `Hard`
- [ ] 719. Find K-th Smallest Pair Distance `Hard`
- [ ] 878. Nth Magical Number `Hard`

---

## Set 4 — Hash Map / Prefix Sum

Default invariant:

```text
Before processing nums[i], the table summarizes exactly nums[0:i].
```

Ask:

- What is stored: value -> index, value -> count, prefix_sum -> count, or canonical key?
- Why is lookup valid before updating the table?

### Must-do

- [x] 1. Two Sum `🔥`
- [x] 49. Group Anagrams
- [x] 128. Longest Consecutive Sequence `🔥`
- [x] 560. Subarray Sum Equals K `🔥`
- [ ] 217. Contains Duplicate
- [ ] 219. Contains Duplicate II
- [ ] 238. Product of Array Except Self
- [ ] 347. Top K Frequent Elements
- [ ] 523. Continuous Subarray Sum
- [ ] 525. Contiguous Array
- [ ] 560. Subarray Sum Equals K `redo until automatic`

---

## Set 5 — BFS / DFS / Trees / Grids Medium Only

Default BFS invariant:

```text
The queue contains the current frontier; nodes marked visited will not be enqueued again.
```

Default DFS invariant:

```text
dfs(node) correctly solves and returns the needed information for this node/subtree/component.
```

Ask:

- What is a node?
- What are the neighbors?
- When do I mark visited: enqueue time or pop time?
- Is the answer returned from recursion, or stored as a best/global value?

### Trees medium/easy-medium

- [ ] 102. Binary Tree Level Order Traversal `🔥`
- [ ] 104. Maximum Depth of Binary Tree
- [ ] 112. Path Sum
- [ ] 199. Binary Tree Right Side View
- [ ] 230. Kth Smallest Element in a BST
- [ ] 235. Lowest Common Ancestor of a BST
- [ ] 236. Lowest Common Ancestor of a Binary Tree `🔥`
- [ ] 543. Diameter of Binary Tree `🔥`
- [ ] 572. Subtree of Another Tree
- [ ] 98. Validate Binary Search Tree `🔥`

### Graphs / grids medium only

- [ ] 200. Number of Islands `🔥`
- [ ] 695. Max Area of Island
- [ ] 733. Flood Fill
- [ ] 994. Rotting Oranges `🔥`
- [ ] 1091. Shortest Path in Binary Matrix
- [ ] 130. Surrounded Regions
- [ ] 133. Clone Graph
- [ ] 207. Course Schedule `🔥`
- [ ] 210. Course Schedule II
- [ ] 417. Pacific Atlantic Water Flow
- [ ] 542. 01 Matrix
- [ ] 785. Is Graph Bipartite?

---

## Set 6 — Heap / Priority Queue Medium Only

Default invariant:

```text
The heap contains the best current candidates according to the priority needed by the problem.
```

Ask:

- Is this top-k, merge-k, scheduling, or shortest-distance style?
- Do I need min-heap, max-heap by negating, or two heaps?
- What item goes into the heap: value, index, pair, count, or distance?

### Must-do

- [ ] 215. Kth Largest Element in an Array `🔥`
- [ ] 347. Top K Frequent Elements `🔥`
- [ ] 373. Find K Pairs with Smallest Sums
- [ ] 378. Kth Smallest Element in a Sorted Matrix
- [ ] 621. Task Scheduler
- [ ] 692. Top K Frequent Words
- [ ] 703. Kth Largest Element in a Stream
- [ ] 973. K Closest Points to Origin `🔥`
- [ ] 1046. Last Stone Weight
- [ ] 1642. Furthest Building You Can Reach

---

## Set 7 — Stack / Monotonic Stack

Default invariant:

```text
The stack stores unresolved indices/items in monotonic order.
```

Ask:

- What candidates are unresolved?
- Is the stack increasing or decreasing?
- What answer becomes known when I pop?

### Must-do

- [ ] 20. Valid Parentheses
- [ ] 71. Simplify Path
- [ ] 150. Evaluate Reverse Polish Notation
- [ ] 155. Min Stack
- [ ] 394. Decode String
- [ ] 739. Daily Temperatures `🔥`
- [ ] 853. Car Fleet

### Hard strength-adjacent

- [ ] 84. Largest Rectangle in Histogram `Hard`

---

## Set 8 — Bitwise / Low-Level / Qualcomm

Default invariant:

```text
At step k, the accumulator contains the correct bit/count/parity state for all processed elements or bit positions.
```

Ask:

- What physical state is represented by the bits?
- Which identity applies: `x ^ x = 0`, `x & (x - 1)` removes the lowest set bit, mask isolates bits?
- Are integers signed, unsigned, fixed-width, or Python-unbounded?

### Must-do

- [x] 136. Single Number `🔥 XOR invariant`
- [x] 268. Missing Number `🔥 XOR or sum`
- [ ] 190. Reverse Bits
- [ ] 191. Number of 1 Bits `🔥`
- [ ] 231. Power of Two
- [ ] 260. Single Number III
- [ ] 338. Counting Bits
- [ ] 371. Sum of Two Integers
- [ ] 389. Find the Difference
- [ ] 461. Hamming Distance
- [ ] 476. Number Complement
- [ ] 693. Binary Number with Alternating Bits

---

# Minimal Must-Do Before Tomorrow

If time is short, do these in order:

1. Redo solved strength problems without looking: **3, 76, 11, 33, 875, 1011**.
2. Add missing medium reps: **15, 42, 209, 239, 704, 34, 74**.
3. Do one BFS, one DFS, one heap: **200, 543, 215**.
4. Do low-level review: **136, 191, 190, 268**.

---

# High-Yield Hints

| Problem | First hint | Invariant to recover |
|---|---|---|
| 76. Minimum Window Substring | Expand until valid, then shrink while still valid. | When updating answer, the window covers all required counts. |
| 33. Search in Rotated Sorted Array | At least one half around `mid` is sorted. | Target, if present, remains in `[lo, hi]`. |
| 875. Koko Eating Bananas | Search speed, not pile index. | Speeds below `lo` are impossible. |
| 1011. Capacity To Ship Packages | Larger capacity never needs more days. | `hi` is feasible; values below `lo` are impossible. |
| 42. Trapping Rain Water | Water depends on smaller of left max and right max. | Move the side with smaller max because it is the limiting side. |
| 239. Sliding Window Maximum | Remove stale indices; keep candidates decreasing. | Deque front is max for current window. |
| 543. Diameter of Binary Tree | Height is returned; diameter is updated separately. | `dfs(node)` returns height; `best` stores largest path seen. |
| 994. Rotting Oranges | Multi-source BFS from all initially rotten oranges. | Queue is the frontier rotting at current minute. |
| 207. Course Schedule | Think indegree, not recursive guessing. | Indegree zero means no remaining prerequisites. |
| 84. Largest Rectangle in Histogram | When a bar is popped, its max width is known. | Stack indices have increasing heights. |

---

# Interview Checklist

Before coding:

- [ ] Restate problem and constraints.
- [ ] Give brute force and cost.
- [ ] Name the pattern.
- [ ] State the invariant.
- [ ] Mention complexity target.

During coding:

- [ ] Keep variable names simple.
- [ ] Update answer only when invariant is true.
- [ ] For BFS, mark visited when enqueuing.
- [ ] For binary search, define `lo`, `hi`, `mid`.
- [ ] For recursion, separate return value from global/best answer.

Testing:

- [ ] Empty/minimum input.
- [ ] One element.
- [ ] Duplicates.
- [ ] Negative numbers if relevant.
- [ ] Already sorted / reverse sorted.
- [ ] Boundary case: window length, index range, disconnected graph, impossible target.

Target speed:

- Easy: 10 minutes.
- Medium: 25–30 minutes.
- Hard: identify pattern, explain invariant, code the core correctly.

---

# One-Sentence Reminders

- Sliding window: expand to include, shrink to restore.
- Two pointers: discard only what you can prove impossible.
- Binary search: define the monotonic predicate first.
- Hash map: ask what you have seen before this index.
- Prefix sum: find the earlier prefix that would make the current range valid.
- DFS/BFS: define node, neighbors, and visited timing.
- Heap: keep only the best candidates needed next.
- Stack: popping means an unresolved candidate just got resolved.
- Bitwise: use identities, masks, and fixed-width reasoning.

*Last updated: 2026-06-01*
