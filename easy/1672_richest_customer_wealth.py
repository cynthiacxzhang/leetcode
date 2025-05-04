# 1672 - Richest Customer Wealth

"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

"""

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        """
        Logic: return all [j] that is associated with customer [i]
        - concept: 2D arrays (matrix)
        - array i is the outer array
        - len(i) = number of customers
        - len(i, j) = number of banks associated with customer i
        """

        # For loop logic: 
        """
        for i in range(rows):
            for j in range(columns):
                process(array[i][j])
        """
        max_wealth = 0

        for i in range(len(accounts)):          # iteration of rows
            current_wealth = 0
            for j in range(len(accounts[i])):   # iteration of columns
                current_wealth += accounts[i][j]
            max_wealth = max(current_wealth, max_wealth)
        return max_wealth


