from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        left = 0
        right = 0

        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for c in s1:
            index = ord(c) - ord('a')
            s1_freq[index] += 1

        for right in range(len(s2)):
            s2_freq[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > window_size:
                s2_freq[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if s1_freq == s2_freq:
                return True
        
        return False
                    
            

            