class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sqsum = self.squareSum(n)
        
        while sqsum not in seen:
            if sqsum == 1: return True

            seen.add(sqsum)
            sqsum = self.squareSum(sqsum)

        return False


    def squareSum(self, n):
        lst = list(map(int, str(n)))
        mysum = 0
        for x in lst:
            mysum += x*x
        return mysum