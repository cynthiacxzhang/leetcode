# 560 Subarray Sum Equals K

"""Given an array of integers nums and an integer k, return the total number of continuous 
subarrays whose sum equals to k.

Solution method: prefix sum with hash map"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # prefix sum method with hash map
        prefix = 0
        result = 0

        seen = {0:1}

        for num in nums: 
            prefix += num

            # prefix = k = nums[num]
            if prefix - k in seen:
                result += seen[prefix - k]

            seen[prefix] = seen.get(prefix, 0) + 1

        return result

        