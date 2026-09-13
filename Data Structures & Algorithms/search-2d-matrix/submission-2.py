class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target:
                low = mid + 1
            else:
                high = mid - 1

        
        return self.binarySearchRow(matrix[high], target)

    def binarySearchRow(self, row, target):
        low = 0
        high = len(row) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if row[mid] > target:
                high = mid - 1
            elif row[mid] < target:
                low = mid + 1
            else:
                return True

        return False
