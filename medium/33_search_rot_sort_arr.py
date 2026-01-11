# Search in rotated sorted array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # simplest, but not within time constraints
        for i, num in enumerate(nums):
            if target == num:
                return i
        return -1

        # proper solution with binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            
            # decide which half is sorted
            if nums[l] <= nums[mid]:
                # lhs sorted
                # if target in lhs range
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: 
                # rhs sorted
                # is target in rhs range
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
        
        return -1

        


