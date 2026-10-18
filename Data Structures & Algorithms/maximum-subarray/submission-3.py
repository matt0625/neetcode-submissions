class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)

        return maxSum
