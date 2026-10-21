class Solution:
    def romanToInt(self, s: str) -> int:
        rmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        res = 0
        for i in range(len(s) - 1, -1, -1):
            res += rmap[s[i]]

            if i != len(s) - 1 and rmap[s[i]] < rmap[s[i + 1]]:
                res -= 2 * rmap[s[i]]

        return res