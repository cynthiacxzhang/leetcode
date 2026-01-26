class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Rolling Merge 
        
        array = sorted(intervals, key=lambda x:x[0])

        # if array empty
        if not array:
            return []

        result = [] # (1, 4) (2, 3)

        curr = array[0]
        
        for i in range(1, len(array)):
            # if overlapping, merge then check again with next array value
            if curr[1] >= array[i][0]:
                curr = (min(curr[0], array[i][0]), max(curr[1], array[i][1]))
                print(curr)
                continue
            
            # if not overlapping (or fully merged), add to result array
            result.append(curr)
            curr = array[i]
        
        result.append(curr)
        
        return result
