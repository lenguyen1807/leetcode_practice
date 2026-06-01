**Pattern**: Hash Map

**State**:
- `seen`: a hash map of `sorted_string -> [original_strings]`.

**Invariant**:
- Before processing `strs[i]`, `seen` maps the sorted representation of each processed string in `strs[0:i]` to its original form group.

**Update Rule**:
- For each string `s` in `strs`, sort its characters to create the canonical key: `sorted_s = "".join(sorted(s))`.
- If `sorted_s` is not in `seen`, initialize it: `seen[sorted_s] = [s]`.
- Else, append `s` to the list: `seen[sorted_s].append(s)`.
