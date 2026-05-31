class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        # 1. Reverse entire array
        reverse(0, n - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse remaining elements
        reverse(k, n - 1)
