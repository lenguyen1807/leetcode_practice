from typing import List
import bisect

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check_capacity(pref, capacity):
            prev_val = 0
            idx = 0
            cnt = 0

            while idx < len(pref):
                idx = bisect.bisect_right(pref, prev_val + capacity)
                prev_val = pref[idx - 1]
                cnt += 1

            return cnt

        # get prefix sum of all packages
        pref = [0] * len(weights)
        for i in range(len(weights)):
            pref[i] = pref[i-1] + weights[i] if i > 0 else weights[i]

        lo = max(weights) # at least we can ship the heaviest package in a day
        hi = sum(weights) # we can ship all packages in a day
        answer = float("inf")

        # O(logN)
        while lo <= hi:
            capacity = lo + (hi - lo) // 2
            cnt = check_capacity(pref, capacity)

            if cnt <= days: # answer
                answer = min(answer, capacity)
                hi = capacity - 1
            else:
                lo = capacity + 1

        return answer
