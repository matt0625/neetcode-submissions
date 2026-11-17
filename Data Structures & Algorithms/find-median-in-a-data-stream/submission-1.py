import heapq
class MedianFinder:
    # two heaps 
    def __init__(self):
        self.lower = []
        self.upper = []

    # add to correct heap side ensuring balance
    def addNum(self, num: int) -> None:
        # always insert to lower first
        heapq.heappush_max(self.lower, num)
        
        # move max element of lower to upper 
        heapq.heappush(self.upper, heapq.heappop_max(self.lower))

        # ensure lower has equal or one less element
        if len(self.upper) > len(self.lower):
            heapq.heappush_max(self.lower, heapq.heappop(self.upper))


    # return the middle value if odd length otherwise the average of eiher side
    def findMedian(self) -> float:
        # invariant: the median value (if n odd) can always be found on the top of the lower heap
        if (len(self.lower) + len(self.upper)) % 2 == 1:
            return float(self.lower[0])

        return (self.lower[0] + self.upper[0]) / 2
        