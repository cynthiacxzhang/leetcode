# Kth Factor of N

"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.


Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

"""

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # Brainstorm
        """
        Step 1: gather all of the factors up to n/2(ceiling), append N itself at list end
        Step 2: check if list has k factors - if not, return -1
        Step 3: list is already sorted, search for kth member (index k - 1) and return k
        """
        factors = []

        for i in range(1, int(n/2) + 1): # range 0 to half of n (biggest possible factor other than n itself)
            if (n % i == 0):
                factors.append(i)

        # debugging
        for i in range(len(factors)):
            print(i)

        factors.append(n)

        if len(factors) < k:
            return -1
        else:
            return factors[k-1]
