class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.operation(op1, op2, item))
            else:
                stack.append(int(item))

        return stack[0]

    def operation(self, op1, op2, operator):
        if operator == '+': return op1 + op2

        elif operator == '-': return op1 - op2

        elif operator == '*': return op1 * op2

        elif operator == '/': return int(op1 / op2)

        return