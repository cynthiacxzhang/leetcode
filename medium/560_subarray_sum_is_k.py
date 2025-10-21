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

        