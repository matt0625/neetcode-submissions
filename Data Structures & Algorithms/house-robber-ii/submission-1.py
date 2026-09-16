class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        case1 = nums[0: len(nums) - 1]
        case2 = nums[1:]

        return max(self.rob_linear(case1), self.rob_linear(case2))

    def rob_linear(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for money in nums:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1
