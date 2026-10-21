class Solution:
    def firstUniqChar(self, s: str) -> int:
        occs = {}
        for i in range(len(s)):
            ch = s[i]
            if ch not in occs:
                occs[ch] = [0, i]

            occs[ch][0] += 1

        for k, v in occs.items():
            if v[0] == 1:
                return v[1]

        return -1
