class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        
        i = 0
        j = len(heights) - 1
        while j - i > 0:
            area = (j-i) * min(heights[i], heights[j])
            max_a = max(area, max_a)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_a