class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # use one pass to populate an array at index i where arr[i] is the cost of swapping from s[i] to t[i]

        arr = [0] * len(s)
        for i in range(len(s)):
            arr[i] = abs(ord(s[i]) - ord(t[i]))

        # now this turns into a maximum subarray with sum k problem
        # sliding window

        left = 0
        right = 0
        curCost = 0
        maxLen = 0

        while right < len(arr):
            curCost += arr[right]
            
            while curCost > maxCost:
                curCost -= arr[left]
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
            
            right += 1

        return maxLen
            

