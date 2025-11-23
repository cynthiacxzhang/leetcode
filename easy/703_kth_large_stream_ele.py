import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        # k and stream of scores num
        self.k = k
        self.nums = nums
        
        self.heap = []

        # build initial heap based on nums
        # size of heap = k
        # min heap, we push largest values only

        for num in nums:
            # push current value
            heapq.heappush(self.heap, num)
            
            # check if heap exceeds k, and if it does, pops smallest
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
            

    def add(self, val: int) -> int:

        # value we want to add
        curr = val

        heapq.heappush(self.heap, curr)
            
        # check if heap exceeds k, and if it does, pop smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)