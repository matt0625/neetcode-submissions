class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        

        return min(
            self.helper(cost, n - 1, memo),
            self.helper(cost, n - 2, memo)
        )


    def helper(self, cost, start, memo):
        if start <= 1: return cost[start]
        elif start in memo:
            return memo[start]

        else:
            memo[start] = min(self.helper(cost, start-1, memo), self.helper(cost, start-2, memo)) + cost[start]
            return memo[start]

