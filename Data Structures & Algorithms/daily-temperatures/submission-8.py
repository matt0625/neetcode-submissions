class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # strategy: maintain stack storing all seen temperatures that are less than the last global maximum
        # then at each step compare the next top value to the items in the stack and store the amount of items between any stack items it is higher than

        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((curr, i))

        
        return result
                

