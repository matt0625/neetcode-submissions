from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        # original O(n*klogk) approach naive due to sorting
        groups = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
        '''
        # new O(n*k) approach based on each string having a unique char frequency list 
        groups = defaultdict(list)

        for s in strs:
            s_arr = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                s_arr[index] += 1

            key = tuple(s_arr)
            groups[key].append(s)

        return list(groups.values())