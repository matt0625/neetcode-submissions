from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            if self.getTime(piles, mid) > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return low 


    def getTime(self, piles, k):
        time = 0
        for pile in piles:
            time += ceil(pile/k)
        
        return time