class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            # Pivot is to the right of mid
            if nums[mid] > nums[hi]:
                lo = mid + 1
            # Pivot is at mid or to the left of mid
            else:
                hi = mid
                
        return nums[lo]
