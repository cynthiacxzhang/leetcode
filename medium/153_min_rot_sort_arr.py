# Minimum in rotated sorted array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        return min(nums)
        """

        class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        return min(nums)
        """

        # proper solution using binary search
        l, r = 0, len(nums)-1

        while l < r: # cannot overlap since rhs is being set at mid, and not mid - 1
            mid = (l+r) // 2

            if nums[r] < nums[mid]:
                # min in rhs
                l = mid + 1
            else:
                # min = mid or in lhs
                r = mid
        
        # l = mid = r when this happens
        return nums[l]
            

