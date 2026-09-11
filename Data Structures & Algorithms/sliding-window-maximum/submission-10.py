class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        right = k - 1
        current_max = max(nums[0:k])

        while right < len(nums) - 1:
            res.append(current_max)
            right += 1
            if nums[right] > current_max:
                current_max = nums[right]

            if nums[left] == current_max:
                if left + k <= len(nums):
                    current_max = max(nums[left + 1:right + 1])
                else:
                    current_max = max(nums[left + 1:len(nums)])

            left += 1
        
        res.append(current_max)
        return res
            
