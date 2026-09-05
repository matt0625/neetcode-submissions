class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        srted = sorted(numbers)
        left = 0
        right = len(srted) - 1
        while left < right:
            l = srted[left]
            r = srted[right]
            if l + r > target:
                right -= 1
            elif l + r < target:
                left += 1

            else:
                return [left + 1, right + 1]