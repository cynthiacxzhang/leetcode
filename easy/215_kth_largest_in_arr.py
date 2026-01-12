class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq   
        heapq.heapify(nums)

        # while there are more than k values in the min-heap
        while len(nums) > k:
            heapq.heappop(nums) # popping root = popping min value 
        
        # root that remains is the kth largest 

        return heapq.heappop(nums)