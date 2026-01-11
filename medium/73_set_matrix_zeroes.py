# Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # track row/cols with set
        rows_to, cols_to = set(), set()

        rows, cols = len(matrix), len(matrix[0])

        # first pass - store rows and columns with zeroes in sets
        for R in range(rows):
            for C in range(cols):
                if matrix[R][C] == 0:
                    rows_to.add(R)
                    cols_to.add(C)
        
        # second pass - zero cells if their row or col is marked
        for R in range(rows):
            for C in range(cols):
                if R in rows_to or C in cols_to:
                    matrix[R][C] = 0
        
        