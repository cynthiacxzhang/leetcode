class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
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
        

        