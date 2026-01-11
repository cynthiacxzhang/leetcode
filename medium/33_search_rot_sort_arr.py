# Search in rotated sorted array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # simplest, but not within time constraints
        for i, num in enumerate(nums):
            if target == num:
                return i
        return -1

        # proper solution

        


