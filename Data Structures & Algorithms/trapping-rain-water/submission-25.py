class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0

        while left < right:
            while left < right and height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total += max_left - height[left]
                left += 1

            while left < right and height[right] <= height[left]:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total += max_right - height[right]
                right -= 1

            '''
            while left < right and height[left] == height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total += max_left - height[left]
                
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total += max_right - height[right]

                left += 1
                right -= 1

            '''
            

        return total 

            

                

            