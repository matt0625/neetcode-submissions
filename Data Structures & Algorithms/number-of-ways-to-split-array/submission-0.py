class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # make a prefix array left which is where left[i] = sum(left[0:1-i])
        # similar for right
        # then do a single scan comparison

        left = [0] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] + left[i-1]

        right = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i+1] + right[i+1]

        count = 0
        for i in range(len(nums) - 1):
            if left[i] + nums[i] >= right[i]:
                count += 1

        return count
