# Container with the Most Water

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # Brainstorm
        """
        Input: list of heights
        Output: volume of water contained between the two tallest (and furthest) bars
        - e.g. height of the shorter of two bars * distance between bars (in the list)

        Brute Force Method: double iteration through list
        - iterate twice to get the two highest values in the heights list
        - compute area between all possible combinations of heights
        - O(n2) time, not optimal at all

        Optimal Method: two pointers
        - two pointers, one going right from i = 0, one going left from i = -1
        - for each pointer movement, compute current_area between the two locations
            - store this area in a "area" variable
        - move the smaller pointer value (in whatever direction it applies to) 
            - compute current_area again
            - compare current_area to "current_area" and set area = max(current_area, area)
        - move until the indexes of the two pointers meet
        - return area

        """