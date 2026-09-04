from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freqs = [[] for i in range(len(nums) + 1)]
        for num, v in count.items():
            freqs[v].append(num)

        res = []
        i = len(nums)
        while len(res) < k:
            curr = freqs[i]
            for j in range(len(curr)):
                res.append(curr[j])
                if len(res) == k:
                    break
            i -= 1
        return res