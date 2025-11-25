class Solution:
    def maxArea(self, height: List[int]) -> int:

        
        # helper to compute volume 
        def get_vol(left, right):
            
            width = right - left
            curr_height = min(height[left], height[right])

            return width * curr_height
        
        left, right = 0, len(height) - 1
        best = 0

        # two pointer logic, start with largest width
        while left < right:

            curr_vol = get_vol(left, right)
            best = max(curr_vol, best)

            # always move smaller height - greedy option
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return best
            

            




