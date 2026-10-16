class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        local_min = float('inf')

        for price in prices:
            local_min = min(local_min, price)
            max_profit = max(max_profit, price-local_min)

        return max_profit