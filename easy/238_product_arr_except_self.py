class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        prefix product - brainstorm

        left and right arrays to track prefix sums from either direction
        - inclusive? or unique prefixes wanted?
        ans[i] = left[i-1] * right[1+1]
        """

        # build left and right prefix product arrays
        n = len(nums)
        left, right = [0] * n, [0] * n

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i]
        
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j]

        # building answer array
        ans = [0] * n

        # edge cases
        ans[0] = right[1]
        ans[-1] = left[-2]

        for k in range(1, len(nums) - 1):
            ans[k] = left[k-1] * right[k+1]
        
        return ans