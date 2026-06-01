import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on eating speed
        lo = 1
        hi = max(piles)
        answer = float("inf")
        while lo <= hi:
            k = lo + (hi - lo) // 2
            # we track the piles
            t = sum([math.ceil(p / k) for p in piles])
            if t <= h: # we need to decrease our k
                answer = min(answer, k)
                hi = k - 1
            else:
                lo = k + 1
        return answer
