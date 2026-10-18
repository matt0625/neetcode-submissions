class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k == 1: return max(nums)
        left = 0
        right = 0
        mysum = nums[0]
        max_sum = float('-inf')

        last_seen = {nums[0] : 0}
        while right < len(nums)-1:
            right += 1
            if nums[right] in last_seen and last_seen[nums[right]] >= left:
                while left <= last_seen[nums[right]]:
                    mysum -= nums[left]
                    left += 1
                
            last_seen[nums[right]] = right
            mysum += nums[right]
                
            if right - left + 1 > k:
                mysum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(mysum, max_sum)

        if max_sum == float('-inf'): return 0
        return max_sum

                


