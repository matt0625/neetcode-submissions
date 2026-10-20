class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # nlogn with sorting and pairing smallest with largest, making that the target
        skill.sort()
        target = skill[0] + skill[-1]
        left, right = 1, len(skill) - 2
        totalChem = skill[0] * skill[-1]
        while left <= right:
            if skill[left] + skill[right] != target:
                return -1

            totalChem += skill[left] * skill[right]
            left += 1
            right -= 1

        return totalChem


