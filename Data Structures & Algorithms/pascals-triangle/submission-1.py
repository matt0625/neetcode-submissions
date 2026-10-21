class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        row_ptr = 0
        while len(res) < numRows:
            row = [1]
            for i in range(1, len(res) + 1):
                if i >= len(res[row_ptr]):
                    row.append(1)
                else:
                    row.append(res[row_ptr][i-1] + res[row_ptr][i])

            res.append(row)
            row_ptr += 1

        return res