class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        
        i = 0
        j = len(heights) - 1
        while j - i > 0:
            area = (j-i) * min(heights[i], heights[j])
            max_a = max(area, max_a)

            if heights[j] == min(heights[i], heights[j]):
                j -= 1
            else:
                i += 1

        return max_a