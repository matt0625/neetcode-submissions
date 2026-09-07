class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1

        left = 0
        right = 1
        last_seen = {}
        last_seen[s[left]] = 0

        while right < len(s):
            if s[right] in last_seen:
                max_length = max(max_length, right - left)
                left = max(left, last_seen[s[right]] + 1)

            last_seen[s[right]] = right
            right += 1

        max_length = max(max_length, right - left)
        return max_length