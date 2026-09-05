class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for num in seen:
            if num - 1 in seen:
                continue
            else:
                count = 1
                val = num
                while val + 1 in seen:
                    count += 1
                    val += 1

                if count > longest:
                    longest = count

        return longest
