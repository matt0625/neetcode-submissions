class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        srted = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and srted[i] == srted[i-1]:
                continue
            curr = srted[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                l = srted[left]
                r = srted[right]
                if curr + l + r > 0:
                    right -= 1
                elif curr + l + r < 0:
                    left += 1

                else:
                    res.append([curr, l, r])

                    left += 1
                    right -= 1

                    while left < right and r == srted[right]:
                        right -= 1
                    while left < right and srted[left] == l:
                        left += 1
                

        return res