class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        acc = len(nums)
        for i, n in enumerate(nums):
            acc ^= (i ^ n)
        return acc