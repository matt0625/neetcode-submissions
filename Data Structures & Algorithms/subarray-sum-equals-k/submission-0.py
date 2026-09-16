class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        prefixes = {0:1}

        for n in nums:
            current_sum += n
            diff = current_sum - k

            res += prefixes.get(diff, 0)
            prefixes[current_sum] = 1 + prefixes.get(current_sum, 0)
        
        return res