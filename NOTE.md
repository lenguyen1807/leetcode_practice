# Algorithmic Techniques & Notes

## Two-Pointer vs. Sliding Window

While "Sliding Window" is a specialized sub-category of the "Two-Pointer" technique, they represent distinct mental models and structural patterns.

---

### 1. Two-Pointer Technique (A Broad Strategy)
The two-pointer technique uses two independent indices to traverse one or more linear data structures. The pointers can move in different directions, at different speeds, or even on different arrays.

#### Opposite-Direction (Converging)
Pointers start at opposite ends (`left = 0`, `right = N - 1`) and move toward each other until they meet.
* **Usage**: Finding pairs in a sorted array (Two Sum II), reversing an array, binary search, or partitioning in QuickSort.
* **Mechanism**: You evaluate the boundary elements at `arr[left]` and `arr[right]` to make a binary decision on which pointer to move. The space between them is not "tracked" as an aggregate state.

#### Same-Direction (Fast/Slow or Runner)
Both pointers start at the same end but move at different rates or under different conditions.
* **Usage**: Cycle detection (Floyd’s Tortoise and Hare), removing duplicates in-place, or finding the middle of a linked list.

---

### 2. Sliding Window Technique (Contiguous Aggregates)
Sliding Window is a **same-direction two-pointer pattern** where the two pointers (`start` and `end`) strictly define the boundaries of a **contiguous subsegment (a "window")**: `arr[start:end+1]`.

* **Contiguous Window State**: You maintain a dynamic aggregate state of *every* element inside the window (e.g., a running sum, character frequency map, or distinct count). When `end` expands, you add the new element's contribution. When `start` shrinks, you subtract the left element's contribution.
* **Monotonic Same-Direction Movement**: Both pointers move monotonically from left to right. They never move toward each other, and they never cross.

---

### Comparison Summary

| Attribute | Two-Pointer (Opposite-Direction) | Sliding Window (Same-Direction) |
| :--- | :--- | :--- |
| **Contiguity** | The elements *between* the pointers do not need to be tracked or form a cohesive state. | The elements *between* the pointers form a strictly contiguous subarray whose aggregate state must be maintained. |
| **Pointer Movement** | Pointers move toward each other (`left++`, `right--`). | Both pointers move in the same direction (`end++` to expand, `start++` to shrink). |
| **Decision Rule** | A simple comparison of `arr[left]` and `arr[right]` determines which pointer to move. | The validity of the window's aggregate state determines when to expand (outer loop) or shrink (inner `while` loop). |
| **Common Target** | Finding a specific pair, boundary, or partition. | Finding the longest, shortest, or most optimal contiguous subarray satisfying a condition. |
