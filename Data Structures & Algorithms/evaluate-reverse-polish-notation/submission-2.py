class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ("+", "-", "*", "/"):
                recent = stack.pop()
                prev = stack.pop()
                if c == "+":
                    res =prev + recent
                elif c == "-":
                    res = prev - recent
                elif c == "*":
                    res = prev * recent
                else:
                    res = int(prev / recent)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack.pop()
            

        