class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False
        '''

        # upon the first iteration mark entries which are turned to 0 with an X
        # this is a flag that tells us: we shouldn't change this [r, c] to 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for i in range(cols):
                        if matrix[r][i] != 0: matrix[r][i] = 'X'
                    for j in range(rows):
                        if matrix[j][c] != 0: matrix[j][c] = 'X'


        # at this point matrix contains Xs for every value which should rightfully be changed to a 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 'X': matrix[r][c] = 0
        '''

        # strategy: use first row and col to denote if that row or column needs to change to a 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True


        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
         