class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    

        # optimal: do binary search to find the row as well
        # find which row range (row[0] and row[-1]) the target falls into with BS
        # find which exact row index it is with BS on that row


        for row in matrix:
            if row[0] <= target <= row[-1]:
                # bin search on this list
                left, right = 0, len(row) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] <= target:
                        left = mid + 1
                    else: 
                        right = mid - 1
        
        return False
        

        