class Solution:

    def encode(self, strs: List[str]) -> str:
        # can't use a simple delimiter, not even \n as they all have unicode values that could be in the list of strings
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        tmp = ""
        left = 0
        while left < len(s):
            if s[left] == '#':
                length = int(tmp)
                tmp = ""
                res.append(s[left + 1: left + length + 1])
                left = left + length + 1

            else:
                tmp += s[left]
                left += 1

        return res