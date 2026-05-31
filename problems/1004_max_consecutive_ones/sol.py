class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        freq = {}
        max_len = 0

        for end in range(len(nums)):
            bit = nums[end]
            freq[bit] = freq.get(bit, 0) + 1

            while start <= end and freq.get(0, 0) > k:
                freq[nums[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
