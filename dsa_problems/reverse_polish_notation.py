import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for e in range(len(tokens)):
            if tokens[e] not in operators:
                stack.append(int(tokens[e]))
            else:
                second = stack.pop()
                first = stack.pop()
                tmp = 0
                if tokens[e] == "+":
                    tmp = first + second
                elif tokens[e] == "-":
                    tmp = first - second
                elif tokens[e] == "*":
                    tmp = first * second
                elif tokens[e] == "/":
                    tmp = int(first / second)

                stack.append(tmp)

        return stack[-1]
