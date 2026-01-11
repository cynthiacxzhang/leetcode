class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # brute force - all subarrays and sums - TLE
        """
        max_sum = nums[0]
        n = len(nums)
        
        for i in range(0, n):
            # resets to prevent loop carryover
            curr_sum = 0

            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum
        """

        # kadane's algorithm - smarter way of judging reset point
        # if adding nums[i] makes curr_sum negative, it's better just to start over with the current x
        # this rule holds unless the current x is words than curr_sum
        # in which case, just append it and keep going

        max_sum = nums[0]
        curr_sum = 0

        # pointers, rhs is implicit, lhs (j) is iterative
        for j in range(len(nums)):
            # if curr is negative and less than current value in array, reset
            if curr_sum < 0 and curr_sum < nums[j]:
                curr_sum = nums[j]

            # else, add current value onto running sum
            else:
                curr_sum += nums[j]
            
            max_sum = max(max_sum, curr_sum)

        return max_sum







        