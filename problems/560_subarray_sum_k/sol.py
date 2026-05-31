class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1} # base case: S[-1] = 0 prefix sum seen once
        curr_sum = 0
        count = 0
        
        for n in nums:
            curr_sum += n
            if curr_sum - k in seen:
                count += seen[curr_sum - k]
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
            
        return count
