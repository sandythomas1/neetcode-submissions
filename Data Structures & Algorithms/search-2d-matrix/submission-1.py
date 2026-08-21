class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #always check the first value of each row
        #not sure if i would need a mid for this problem 
        top = 0
        bottom = len(matrix) - 1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        if not top <= bottom:
            return False

        l = 0
        r = len(matrix[mid]) - 1

        while l <= r:
            col_mid = (l + r) // 2
            if matrix[mid][col_mid] == target:
                return True
            elif matrix[mid][col_mid] < target:
                l = col_mid + 1
            else:
                r = col_mid - 1
        return False 
            
       