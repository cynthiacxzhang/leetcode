class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        new_arr = []
        
        e1 = nums[0]
        nums = nums[1:]

        for i, num in enumerate(nums):
            new_arr.append((i, num))
        
        new_arr = sorted(new_arr, key=lambda x: x[1])

        result = e1 + new_arr[0][1] + new_arr[1][1]

        return result
       
       


        
        


