class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        2 pointers
        - 1 iterating whole array
        - 1 tracking nonzero elements
        """

        size = len(nums)
        count = 0

        # slow tracks loc of next nonzero element
        slow = 0
        fast = 0

        # fast is an index
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        # starting from where the last nonzero item is
        print(slow)
        for i in range(slow, len(nums)):
            nums[i] = 0

        return nums


                
            
                
