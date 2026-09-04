class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)

        '''
        # naive O(n) time but also O(n) space
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        right = [1] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i + 1]

        for i in range(n):
            output.append(left[i] * right[i])
        

        return output
        '''
        # O(1) space strategy: do everything in place in 2 passes
        # first pass stores left values in output
        # 2nd pass multiplies in right values from a counter
        left = 1
        output.append(left)
        for i in range(1, n):
            left *= nums[i-1]
            output.append(left)

        right = 1
        for i in range(n-2, -1, -1):
            right *= nums[i+1]
            output[i] *= right

        return output
    
