# Best time to buy and sell stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # brute force method
        """
        double array iteration, finding lowest buy price and highest sell price after buy date
        """

        # optimal method: sliding window
        left, right = prices[0], prices[1]
        max_profit = 0
        curr_profit = right - left

        for price in prices[1:]:
            right = price
            curr_profit = right - left

            # negative profit, move left pointer to right pointer
            if curr_profit < 0:
                left = right
            else:
                max_profit = max(max_profit, curr_profit)
            
        return max_profit

# better method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low, best = prices[0], 0

        for price in prices:

            diff = price - low
            print(diff)

            # update low
            if diff <= 0:
                low = price
            # 
            else: 
                best = max(best, diff)
        
        return best

            
