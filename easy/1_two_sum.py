# Twosum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
    

# hash map implementation 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        x + y = target
        y = target - x

        have we seen target-x before? track in a map 
        (not set since sets are unordered and we need to know the index!)
        """

        seen = dict()

        for i, x in enumerate(nums): 
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        
    


