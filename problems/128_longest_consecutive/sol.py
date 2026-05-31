class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums_set = set(nums)
        max_len = 0

        for n in nums_set:
            if n - 1 not in nums_set:  # n is a sequence start
                current_num = n
                current_len = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_len += 1
                max_len = max(max_len, current_len)
                
        return max_len
