import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = [0] * 26
        s = s.lower()

        left = 0
        right = 0
        window_size = 0
        max_window_size = 1

        freqs[ord(s[0]) - ord('a')] += 1
        max_freq = 1

        while right < len(s) - 1:
            right += 1
            window_size = right - left + 1
        
            ind = ord(s[right]) - ord('a')
            freqs[ind] += 1
            if freqs[ind] > max_freq:
                max_freq = freqs[ind]
                

            if window_size - max_freq > k:
                freqs[ord(s[left]) - ord('a')] -= 1
                left += 1
            else:
                if window_size > max_window_size:
                    max_window_size = window_size
        
        return max_window_size

