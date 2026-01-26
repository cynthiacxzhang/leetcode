# Naive solution: store all numbers in an array, sort it when finding median

class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        # print(self.arr) # for debugging
        

    def findMedian(self) -> float:
        curr_arr = self.arr
        curr_arr.sort()
        curr_size = len(curr_arr)

        rhs = curr_size // 2

        if curr_size % 2 != 0:
            return curr_arr[rhs]
        else:
            return (curr_arr[rhs] + curr_arr[rhs - 1]) / 2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Optimized solution: use two heaps to track lower and upper halves of data stream
class MedianFinder:

    import heapq

    def __init__(self):
        
        # double heap tracking method
        self.upper = []
        self.lower = []
        

    def addNum(self, num: int) -> None:
        
        # add to upper if value is greater than max of lower
        if self.lower and -num <= self.lower[0]: # since lower is max heap in negatives
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        # rebalance if heaps differ in size by more than 1
        if len(self.upper) > len(self.lower) + 1:
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -val) # push negative value

        if len(self.lower) > len(self.upper) + 1:
            val = (-1)*heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
            

    def findMedian(self) -> float:

        # heaps solution
        print(len(self.lower))
        print(len(self.upper))

        if (len(self.lower) + len(self.upper)) % 2 == 0:
            return (-(self.lower[0]) + self.upper[0]) / 2

        if len(self.lower) > len(self.upper):
            print(self.lower[0])
            return (-1)*self.lower[0]
        
        return self.upper[0]




        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()