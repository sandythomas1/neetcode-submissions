class Solution:
    def isValid(self, s: str) -> bool:
        CTO = {')' : '(', '}' : '{', ']' : '['}
        res = []

        for c in s: 
            if c not in CTO:
                res.append(c)
            else:
                if not res:
                    return False
                elif res[-1] != CTO[c]:
                    return False
                elif res[-1] == CTO[c]:
                    res.pop()
        if res:
            return False
        else:
            return True