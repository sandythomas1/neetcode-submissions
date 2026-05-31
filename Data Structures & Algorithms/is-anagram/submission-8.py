class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #cant be if not same length
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        