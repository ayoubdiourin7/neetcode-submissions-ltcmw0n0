class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ("+","-","/","*"):
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    res= second+first
                if token == "*":
                    res= second*first
                if token == "/":
                    res= int(first/second)
                if token == "-":
                    res= first-second
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]

        