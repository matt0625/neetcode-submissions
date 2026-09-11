from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = None
        left = 0
        right = -1

    
        t_freq = defaultdict(int)
        sat_req = len(set(t))
        satisfied = 0
        s_freq = defaultdict(int)

        for c in t:
            t_freq[c] += 1
            
        while right < len(s) - 1:
            right += 1
            s_freq[s[right]] += 1

            if s_freq[s[right]] == t_freq[s[right]]:
                satisfied += 1

                while satisfied == sat_req:

                    if res is None or right - left + 1 < len(res):
                        res = s[left:right + 1]

                    s_freq[s[left]] -= 1

                    if s_freq[s[left]] < t_freq[s[left]]:
                        satisfied -= 1
                    left += 1
        
        if res is None: return ""

        return res

            

            

