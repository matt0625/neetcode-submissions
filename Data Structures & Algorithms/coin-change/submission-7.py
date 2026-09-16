class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        res = self.recursiveCoinChange(coins, amount, memo)
        if res == float('inf'): return -1

        return res

    def recursiveCoinChange(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        if amount in memo:
            return memo[amount]

        best = float('inf')
        for coin in coins:
            if coin <= amount:
                best = min(best, self.recursiveCoinChange(coins, amount-coin, memo) + 1)

        memo[amount] = best
        return best

