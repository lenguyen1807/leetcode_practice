**Pattern**: Bitwise

Note that, we need to remember `XOR` properties:
1. `a XOR 0 = a`
2. `a XOR a = 0`

**State**: `acc`, a single accumulator.

**Invariant**: At each iteration `k`, `acc` will be the result of `arr[k] XOR acc(arr[0:k])`. 

**Update Rule**: To process  nums[k] , we update:
$$
\text{acc} = \text{acc} \oplus \text{nums}[k]
$$
If `nums[k]` is the second occurrence of a number, it will pair with the first and both will vanish to $0$. If it is the first, it remains in  acc  as an unmatched element. The invariant holds.