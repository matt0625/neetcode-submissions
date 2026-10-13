class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        num = str(num)
        res = []
        for dig in num:
            res.append(int(dig))

        return res
          

        