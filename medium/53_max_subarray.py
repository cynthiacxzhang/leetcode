# max subarray problem



# brute force solution - nested loop with O(n^2) time complexity
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # note: will need to move left pointer too

        max_sum = nums[0]
        n = len(nums)
        
        for i in range(0, n):
            # resets to prevent loop carryover
            curr_sum = 0

            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum
        
# optimal solution - Kadane's algorithm with O(n) time complexity