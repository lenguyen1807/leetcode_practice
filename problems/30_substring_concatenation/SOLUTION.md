**Pattern**: Sliding Window (aligned by `word_len`)

**State**:
- `offset`: uniform length of a single word in `words`.
- `total_len`: total character length of the concatenated substring (`len(words) * offset`).
- `freq_w`: frequency map of each word in `words`.
- `freq_s`: frequency map of words in the active window `s[start : end + offset]`.
- `start`: start index of the sliding window pass.

**Invariant**:
- The active window `s[start : end + offset]` contains only words whose frequencies do not exceed their budget in `freq_w`.
- Therefore, if the window length `(end + offset - start)` matches `total_len`, it is a valid concatenation.

**Update Rule**:
- Run the sliding window algorithm exactly `offset` times starting from `i` in `range(offset)` to cover all possible mod-alignment remainders:
  - Slide `end` by `offset` steps.
  - Add `sub_w = s[end : end + offset]` to `freq_s`.
  - While `freq_s[sub_w] > freq_w.get(sub_w, 0)`, remove `left_w = s[start : start + offset]` from the window by incrementing `start` by `offset` and decrementing its count.
  - If the window length `(end + offset - start) == total_len`, record `start`.
