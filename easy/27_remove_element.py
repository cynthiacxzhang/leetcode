# Remove Element




class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # Brainstorm
        """
        nums is unsorted, integer val is assumed to be a number in vals
        linear search is best solution since it's not sorted
        keep a counter for any number of vals found, then subtract from len(nums) to get k
        """
        count = 0
        original_length = len(nums)

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                count += 1
            print(count)
        k = len(nums)
        return k

                