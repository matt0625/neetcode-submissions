class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srted = [str(sorted(s)) for s in strs]
        groups = {}

        for i in range(len(srted)):
            if srted[i] not in groups:
                groups[srted[i]] = []

            groups[srted[i]].append(i)

        res = []
        tmp = []
        for v in groups.values():
            for index in v:
                tmp.append(strs[index])
            
            res.append(tmp)
            tmp = []

        return res